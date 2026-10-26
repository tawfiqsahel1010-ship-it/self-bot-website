import os
import time
import secrets
import hashlib
import sqlite3
from pathlib import Path
from fastapi import FastAPI, Header, HTTPException, Query
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI(title="SELF BOT", docs_url=None, redoc_url=None)

BOT_STATUS_KEY = os.getenv("BOT_STATUS_KEY", "")
DB_PATH = Path(os.getenv("CONNECTION_DB", "/tmp/selfbot_requests.db"))
DB_PATH.parent.mkdir(parents=True, exist_ok=True)
REQUEST_TTL = 900
BOT_STATUS = {"last_seen": 0.0}


def connect_db():
    con = sqlite3.connect(DB_PATH, timeout=20)
    con.row_factory = sqlite3.Row
    con.execute("""
        CREATE TABLE IF NOT EXISTS requests (
            request_id TEXT PRIMARY KEY,
            owner_id INTEGER NOT NULL,
            status TEXT NOT NULL,
            capability_hash TEXT NOT NULL,
            created_at REAL NOT NULL,
            expires_at REAL NOT NULL
        )
    """)
    con.commit()
    return con


def check_bot_key(key):
    if not BOT_STATUS_KEY:
        raise HTTPException(503, "BOT_STATUS_KEY is not configured")
    if not key or not secrets.compare_digest(key, BOT_STATUS_KEY):
        raise HTTPException(401, "Unauthorized")


def capability_hash(value):
    return hashlib.sha256(value.encode()).hexdigest()


class Heartbeat(BaseModel):
    status: str = "online"


class NewRequest(BaseModel):
    owner_id: int


class RequestAction(BaseModel):
    request_id: str
    capability: str


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!doctype html><html lang="fa" dir="rtl"><meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <title>SELF BOT</title>
    <body style="font-family:Arial;background:#101827;color:white;text-align:center;padding:50px 18px">
    <h1>SELF BOT</h1><p>ANIL AND TAWFIQ</p>
    <p>مدیریت درخواست‌های اتصال</p>
    <a style="color:#70d6ff" href="/login">پیگیری درخواست</a>
    </body></html>
    """


@app.get("/health")
def health():
    return {"ok": True}


@app.post("/api/bot-heartbeat")
def heartbeat(body: Heartbeat, x_bot_key: str = Header(default="")):
    check_bot_key(x_bot_key)
    if body.status != "online":
        raise HTTPException(400, "Invalid status")
    BOT_STATUS["last_seen"] = time.time()
    return {"ok": True, "status": "online"}


@app.get("/api/bot-status")
def bot_status():
    online = time.time() - BOT_STATUS["last_seen"] < 180
    return {"status": "online" if online else "offline"}


@app.post("/api/connection/create")
def create_request(body: NewRequest, x_bot_key: str = Header(default="")):
    check_bot_key(x_bot_key)
    if body.owner_id <= 0:
        raise HTTPException(400, "Invalid owner")
    request_id = secrets.token_urlsafe(12)
    capability = secrets.token_urlsafe(32)
    now = time.time()

    con = connect_db()
    try:
        con.execute(
            "INSERT INTO requests VALUES (?, ?, ?, ?, ?, ?)",
            (request_id, body.owner_id, "pending",
             capability_hash(capability), now, now + REQUEST_TTL)
        )
        con.commit()
    finally:
        con.close()

    return {
        "request_id": request_id,
        "capability": capability,
        "status": "pending",
        "expires_in": REQUEST_TTL
    }


def get_authorized_request(request_id, capability):
    if not request_id or not capability:
        raise HTTPException(400, "Request ID and capability are required")
    con = connect_db()
    try:
        row = con.execute(
            "SELECT * FROM requests WHERE request_id=?",
            (request_id,)
        ).fetchone()
        if not row:
            raise HTTPException(404, "Request not found")
        if not secrets.compare_digest(
            row["capability_hash"], capability_hash(capability)
        ):
            raise HTTPException(403, "Invalid request access token")
        if row["status"] == "pending" and time.time() > row["expires_at"]:
            con.execute(
                "UPDATE requests SET status='expired' WHERE request_id=?",
                (request_id,)
            )
            con.commit()
            row = con.execute(
                "SELECT * FROM requests WHERE request_id=?",
                (request_id,)
            ).fetchone()
        return dict(row)
    finally:
        con.close()


@app.get("/api/connection/status")
def request_status(
    request_id: str = Query(...),
    capability: str = Query(...)
):
    row = get_authorized_request(request_id, capability)
    return {
        "request_id": row["request_id"],
        "status": row["status"],
        "created_at": int(row["created_at"]),
        "expires_at": int(row["expires_at"])
    }


@app.post("/api/connection/cancel")
def cancel_request(body: RequestAction):
    row = get_authorized_request(body.request_id, body.capability)
    if row["status"] != "pending":
        return {"ok": False, "status": row["status"]}
    con = connect_db()
    try:
        con.execute(
            "UPDATE requests SET status='cancelled' "
            "WHERE request_id=? AND status='pending'",
            (body.request_id,)
        )
        con.commit()
    finally:
        con.close()
    return {"ok": True, "status": "cancelled"}


@app.get("/login", response_class=HTMLResponse)
def login_page(
    request_id: str = Query(default=""),
    capability: str = Query(default="")
):
    rid = request_id.replace("<", "").replace(">", "")
    cap = capability.replace("<", "").replace(">", "")
    return """<!doctype html>
<html lang="fa" dir="rtl"><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>پیگیری درخواست SELF BOT</title>
<body style="font-family:Arial;background:#101827;color:#fff;padding:24px;max-width:600px;margin:40px auto">
<h2>🔐 پیگیری درخواست</h2>
<p>از این صفحه فقط برای مشاهده یا لغو درخواست استفاده کن.</p>
<div id="status">در حال بررسی درخواست...</div>
<button id="refresh">بررسی دوباره</button>
<button id="cancel">لغو درخواست</button>
<p style="color:#ffd166">کد ورود تلگرام، رمز دومرحله‌ای و فایل نشست را در این صفحه وارد نکن.</p>
<script>
const rid = """ + __import__("json").dumps(rid) + """;
const cap = """ + __import__("json").dumps(cap) + """;
const box = document.getElementById("status");
async function refreshStatus(){
  if(!rid || !cap){box.textContent="لینک درخواست ناقص است.";return;}
  try{
    const u="/api/connection/status?request_id="+encodeURIComponent(rid)+"&capability="+encodeURIComponent(cap);
    const r=await fetch(u);
    const d=await r.json();
    box.textContent=r.ok ? "وضعیت درخواست: "+d.status : "درخواست پیدا نشد یا لینک نامعتبر است.";
  }catch(e){box.textContent="ارتباط با سایت برقرار نشد.";}
}
document.getElementById("refresh").onclick=refreshStatus;
document.getElementById("cancel").onclick=async()=>{
  if(!rid || !cap)return;
  try{
    const r=await fetch("/api/connection/cancel",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({request_id:rid,capability:cap})});
    const d=await r.json();
    box.textContent=d.status ? "وضعیت درخواست: "+d.status : "لغو انجام نشد.";
  }catch(e){box.textContent="لغو درخواست انجام نشد؛ دوباره تلاش کن.";}
};
refreshStatus();
</script></body></html>"""
