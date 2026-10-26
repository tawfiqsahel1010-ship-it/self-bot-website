import os
import time
import secrets
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, Header, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI(
    title="SELF BOT | ANIL AND TAWFIQ",
    docs_url=None,
    redoc_url=None,
)

BOT_STATUS_KEY = os.getenv("BOT_STATUS_KEY", "")
BOT_STATUS = {"online": False, "last_seen": 0}
REQUESTS = {}


class HeartbeatPayload(BaseModel):
    status: str = "online"


class ConnectionRequest(BaseModel):
    request_id: str


@app.get("/", response_class=HTMLResponse)
async def home():
    return HTMLResponse(
        '<html lang="fa" dir="rtl"><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        '<title>SELF BOT</title><body style="font-family:Tahoma;text-align:center;'
        'padding:40px;background:#080d1b;color:white">'
        '<h1>SELF BOT</h1><p>ANIL AND TAWFIQ</p>'
        '<a style="color:#65e6ff" href="/login">صفحه اتصال</a>'
        '<p><a style="color:#65e6ff" href="/api/bot-status">وضعیت ربات</a></p>'
        '</body></html>'
    )


@app.post("/api/bot-heartbeat")
async def bot_heartbeat(
    payload: HeartbeatPayload,
    x_bot_key: str = Header(default=""),
):
    if not BOT_STATUS_KEY:
        raise HTTPException(503, "Bot status authentication is not configured")
    if not secrets.compare_digest(x_bot_key, BOT_STATUS_KEY):
        raise HTTPException(401, "Unauthorized")
    if payload.status != "online":
        raise HTTPException(400, "Invalid status")

    BOT_STATUS.update({"online": True, "last_seen": time.time()})
    return {"ok": True}


@app.get("/api/bot-status")
async def bot_status():
    last_seen = BOT_STATUS["last_seen"]
    age = time.time() - last_seen if last_seen else None
    return {
        "website": "online",
        "bot": "online" if age is not None and age < 180 else "offline",
        "last_seen_seconds_ago": int(age) if age is not None else None,
    }


@app.get("/api/connection/status")
async def connection_status(request_id: str):
    item = REQUESTS.get(request_id)
    if not item or item["expires"] < time.time():
        raise HTTPException(404, "Request not found or expired")
    return {"status": item["status"]}


@app.post("/api/connection/cancel")
async def cancel_connection(data: ConnectionRequest):
    item = REQUESTS.get(data.request_id)
    if not item or item["expires"] < time.time():
        raise HTTPException(404, "Request not found or expired")
    item["status"] = "cancelled"
    return {"ok": True, "status": "cancelled"}


@app.get("/login", response_class=HTMLResponse)
async def login_page():
    page = Path(__file__).with_name("login_page.html")
    if not page.is_file():
        raise HTTPException(404, "Login page not found")
    return HTMLResponse(page.read_text(encoding="utf-8"))


@app.get("/health")
async def health():
    return {"ok": True}
