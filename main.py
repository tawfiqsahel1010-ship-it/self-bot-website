from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(
    title="SELF BOT ANIL AND TAWFIQ",
    docs_url=None,
    redoc_url=None
)

@app.get("/", response_class=HTMLResponse)
async def home():
    return HTMLResponse("""
<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#080d1b">
<title>SELF BOT | ANIL AND TAWFIQ</title>
<style>
*{box-sizing:border-box}
body{
 margin:0;min-height:100vh;
 font-family:Tahoma,Arial,sans-serif;
 background:radial-gradient(ellipse at top,#163568 0%,#080d1b 58%);
 color:#fff;display:flex;align-items:center;
 justify-content:center;padding:22px
}
.card{
 width:100%;max-width:520px;text-align:center;
 padding:35px 24px;border:1px solid #284b80;
 border-radius:26px;background:#101a2bdc;
 box-shadow:0 20px 70px #0008
}
.logo{
 width:90px;height:90px;margin:0 auto 20px;
 display:grid;place-items:center;border-radius:25px;
 background:linear-gradient(135deg,#1e90ff,#65e6ff);
 color:#071326;font-size:38px;font-weight:900;
 box-shadow:0 0 35px #168bff55
}
h1{font-size:27px;margin:12px 0}
h1 span{color:#65dfff}
.sub{color:#b8c8e5;line-height:2;font-size:14px}
.features{
 display:grid;gap:12px;margin:25px 0;text-align:right
}
.item{
 background:#17253a;border:1px solid #293e5c;
 border-radius:13px;padding:15px;font-size:14px
}
.notice{
 color:#a9c4e9;font-size:12px;line-height:2;
 border-top:1px solid #293e5c;padding-top:18px
}
footer{color:#7087a9;font-size:11px;margin-top:22px}
</style>
</head>
<body>
<main class="card">
 <div class="logo">S</div>
 <h1><span>SELF BOT</span></h1>
 <h2>ANIL AND TAWFIQ</h2>
 <p class="sub">
  به صفحه رسمی معرفی سلف‌بات خوش آمدید.<br>
  امکانات و راهنمای استفاده را از اینجا دنبال کنید.
 </p>
 <section class="features">
  <div class="item">🤖 معرفی امکانات سلف‌بات</div>
  <div class="item">⚙️ راهنمای تنظیمات و استفاده</div>
  <div class="item">🔐 راهنمای امنیت حساب تلگرام</div>
 </section>
 <p class="notice">
  امنیت حساب شما مهم است. کد ورود و رمز دومرحله‌ای
  خود را در سایت‌های ناشناس وارد نکنید.
 </p>
 <footer>SELF BOT • ANIL AND TAWFIQ</footer>
</main>
</body>
</html>
""")
