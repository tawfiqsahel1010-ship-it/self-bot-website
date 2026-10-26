import os
import time
import secrets
import sqlite3
from pathlib import Path

from fastapi import FastAPI, Header, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI(
    title="SELF BOT | ANIL AND TAWFIQ",
    docs_url=None,
    redoc_url=None,
)

BOT_STATUS_KEY = os.getenv("BOT_STATUS_KEY", "")
DB_PATH = Path(os.getenv("CONNECTION_DB", "/tmp/selfbot_requests.db"))
REQUEST_TTL = 15 * 60

def db():
    con = sqlite3.connect(DB_PATH, timeout=15)
    con.row_factory = sqlite3.Row
    con.execute("""
        CREATE TABLE IF NOT EXISTS requests (
            request_id TEXT PRIMARY KEY,
            owner_id INTEGER NOT NULL,
            status TEXT NOT NULL,
            created_at REAL NOT NULL,
            expires_at REAL NOT NULL
        )
    """)
    con.commit()
    return con

class Heartbeat(BaseModel):
    status: str = "online"

class NewRequest(BaseModel):
    owner_id: int

class RequestAction(BaseModel):
    request_id: str

BOT_STATUS = {"last_seen": 0.0}

def check_bot_key(key):
    if not BOT_STATUS_KEY:
        raise HTTPException(503, "BOT_STATUS_KEY is not configured")
    if not secrets.compare_digest(key or "", BOT_STATUS_KEY):
        raise HTTPException(401, "Unauthorized")

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <!doctype html><html lang="fa" dir="rtl">
    <meta charset="utf-8"><meta name="viewport"
    content="width=device-width,initial-scale=1">
    <title>SELF BOT</title>
    <body style="background:#080d1b;color:white;font-family:Tahoma;
    text-align:center;padding:40px">
    <h1>SELF BOT</h1><p>ANIL AND TAWFIQ</p>
    <a style="color:#65e6ff" href="/login">صفحه اتصال</a>
    <p><a style="color:#65e6ff" href="/api/bot-status">وضعیت ربات</a></p>
    </body></html>
    """

@app.get("/health")
async def health():
    return {"ok": True}

@app.post("/api/bot-heartbeat")
async def heartbeat(
    payload: Heartbeat,
    x_bot_key: str = Header(default="")
):
    check_bot_key(x_bot_key)
    if payload.status != "online":
        raise HTTPException(400, "Invalid status")
    BOT_STATUS["last_seen"] = time.time()
    return {"ok": True}

@app.get("/api/bot-status")
async def bot_status():
    last = BOT_STATUS["last_seen"]
    age = time.time() - last if last else None
    return {
        "website": "online",
        "bot": "online" if age is not None and age < 180 else "offline",
        "last_seen_seconds_ago": int(age) if age is not None else None,
    }

@app.post("/api/connection/create")
async def create_request(
    data: NewRequest,
    x_bot_key: str = Header(default="")
):
    check_bot_key(x_bot_key)
    if data.owner_id <= 0:
        raise HTTPException(400, "Invalid owner_id")

    request_id = secrets.token_urlsafe(24)
    now = time.time()
    with db() as con:
        con.execute(
            "INSERT INTO requests VALUES(?,?,?,?,?)",
            (request_id, data.owner_id, "pending", now, now + REQUEST_TTL),
        )
    return {
        "request_id": request_id,
        "status": "pending",
        "expires_in": REQUEST_TTL,
    }

@app.get("/api/connection/status")
async def connection_status(
    request_id: str,
    x_bot_key: str = Header(default="")
):
    check_bot_key(x_bot_key)
    with db() as con:
        row = con.execute(
            "SELECT status, expires_at FROM requests WHERE request_id=?",
            (request_id,),
        ).fetchone()

    if not row:
        raise HTTPException(404, "Request not found")
    if row["expires_at"] < time.time() and row["status"] == "pending":
        with db() as con:
            con.execute(
                "UPDATE requests SET status='expired' WHERE request_id=?",
                (request_id,),
            )
        return {"status": "expired"}
    return {"status": row["status"]}

@app.post("/api/connection/cancel")
async def cancel_request(
    data: RequestAction,
    x_bot_key: str = Header(default="")
):
    check_bot_key(x_bot_key)
    with db() as con:
        row = con.execute(
            "SELECT status, expires_at FROM requests WHERE request_id=?",
            (data.request_id,),
        ).fetchone()
        if not row:
            raise HTTPException(404, "Request not found")
        if row["expires_at"] < time.time():
            con.execute(
                "UPDATE requests SET status='expired' WHERE request_id=?",
                (data.request_id,),
            )
            return {"ok": False, "status": "expired"}
        if row["status"] != "pending":
            return {"ok": False, "status": row["status"]}
        con.execute(
            "UPDATE requests SET status='cancelled' WHERE request_id=?",
            (data.request_id,),
        )
    return {"ok": True, "status": "cancelled"}

@app.get("/login", response_class=HTMLResponse)
async def login_page():
    page = Path(__file__).with_name("login_page.html")
    if not page.is_file():
        raise HTTPException(404, "Login page not found")
    return HTMLResponse(page.read_text(encoding="utf-8"))
