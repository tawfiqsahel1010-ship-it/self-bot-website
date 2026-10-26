from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(
    title="SELF BOT | ANIL AND TAWFIQ",
    docs_url=None,
    redoc_url=None
)

@app.get("/", response_class=HTMLResponse)
async def home():
    return HTMLResponse(r"""
<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#080d1b">
<meta name="description" content="SELF BOT ANIL AND TAWFIQ - معرفی امکانات، راهنما و امنیت تلگرام">
<title>SELF BOT | ANIL AND TAWFIQ</title>
<style>
:root{--bg:#080d1b;--card:#101a2b;--blue:#278cff;--cyan:#65e6ff;--text:#f5f8ff;--muted:#a9bbd7;--border:#243a5c}
*{box-sizing:border-box;scroll-behavior:smooth}
body{margin:0;font-family:Tahoma,Arial,sans-serif;background:radial-gradient(ellipse at top,#173568 0%,var(--bg) 55%);color:var(--text);line-height:1.9}
button,a{font:inherit}
a{color:inherit;text-decoration:none}
header{position:sticky;top:0;z-index:10;background:#080d1beF;border-bottom:1px solid var(--border);backdrop-filter:blur(15px)}
.nav{max-width:1100px;margin:auto;padding:13px 20px;display:flex;align-items:center;justify-content:space-between;gap:12px}
.brand{font-weight:900;color:var(--cyan);letter-spacing:.5px}
.navright{display:flex;align-items:center;gap:15px}
.nav a{font-size:13px;color:#d8e5fb}
.lang{border:1px solid #31517e;background:#152541;color:white;padding:7px 11px;border-radius:10px;cursor:pointer}
main{max-width:1100px;margin:auto;padding:35px 20px 60px}
.hero{text-align:center;padding:55px 12px 45px}
.logo{width:92px;height:92px;margin:auto auto 22px;border-radius:28px;display:grid;place-items:center;background:linear-gradient(135deg,#1e90ff,#65e6ff);color:#071326;font-size:42px;font-weight:1000;box-shadow:0 0 45px #168bff55}
.badge{display:inline-block;border:1px solid #31517e;background:#14233b;color:var(--cyan);border-radius:30px;padding:5px 14px;font-size:12px}
h1{font-size:clamp(32px,6vw,55px);line-height:1.35;margin:17px 0 5px}
h1 span{color:var(--cyan)}
.hero h2{font-size:17px;letter-spacing:2px;color:#d6e6ff;margin:0 0 18px}
.lead{max-width:650px;margin:15px auto 25px;color:var(--muted);font-size:15px}
.buttons{display:flex;justify-content:center;gap:12px;flex-wrap:wrap;margin-top:24px}
.btn{display:inline-block;padding:12px 20px;border-radius:12px;font-weight:bold;font-size:14px;transition:.2s}
.primary{background:linear-gradient(120deg,#218bff,#5bdcff);color:#071326}
.secondary{border:1px solid #36527a;background:#14223a;color:white}
.btn:hover{transform:translateY(-2px)}
.section{margin-top:48px}
.section-title{text-align:center;margin-bottom:24px}
.section-title h2{font-size:27px;margin:0 0 5px}
.section-title p{color:var(--muted);font-size:13px;margin:0}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:15px}
.box{background:linear-gradient(145deg,#13213a,#0e1727);border:1px solid var(--border);border-radius:18px;padding:22px}
.icon{font-size:29px}
.box h3{font-size:16px;margin:8px 0}
.box p{font-size:13px;color:var(--muted);margin:0}
.steps{counter-reset:step}
.step{position:relative;padding:17px 55px 17px 15px;margin-bottom:12px;border:1px solid var(--border);background:#101a2b;border-radius:14px}
.step:before{counter-increment:step;content:counter(step);position:absolute;right:15px;top:17px;width:27px;height:27px;display:grid;place-items:center;background:#1e8bff;color:#071326;font-weight:bold;border-radius:9px}
.notice{border:1px solid #725b2b;background:#332817;border-radius:16px;padding:20px;color:#ffe9b3;font-size:13px}
.notice strong{display:block;margin-bottom:7px;font-size:15px}
.faq details{border:1px solid var(--border);background:#101a2b;border-radius:12px;padding:14px 17px;margin:10px 0}
.faq summary{cursor:pointer;font-weight:bold;font-size:14px}
.faq details p{font-size:13px;color:var(--muted);margin-bottom:0}
.contact{padding:30px 20px;text-align:center;background:linear-gradient(135deg,#142e50,#101a2b);border:1px solid #31517e;border-radius:22px}
.contact p{color:var(--muted);font-size:14px}
footer{text-align:center;border-top:1px solid var(--border);padding:25px 15px;color:#8095b7;font-size:12px}
footer span{color:var(--cyan)}
[hidden]{display:none!important}
@media(max-width:650px){.nav{padding:12px}.navright{gap:9px}.nav a{font-size:11px}.hero{padding-top:35px}main{padding-left:14px;padding-right:14px}.section-title h2{font-size:23px}}
</style>
</head>
<body>
<header>
<nav class="nav">
<a class="brand" href="#home">✦ SELF BOT</a>
<div class="navright">
<a href="#features" data-fa="امکانات" data-en="Features">امکانات</a>
<a href="#guide" data-fa="راهنما" data-en="Guide">راهنما</a>
<a href="#security" data-fa="امنیت" data-en="Security">امنیت</a>
<button class="lang" onclick="toggleLang()">EN / دری</button>
</div>
</nav>
</header>

<main>
<section class="hero" id="home">
<div class="logo">S</div>
<div class="badge" data-fa="نسل جدید تجربه تلگرام" data-en="A new Telegram experience">نسل جدید تجربه تلگرام</div>
<h1><span>SELF BOT</span></h1>
<h2>ANIL AND TAWFIQ</h2>
<p class="lead" data-fa="به صفحه رسمی SELF BOT خوش آمدید. امکانات پروژه، راهنمای شروع و نکته‌های مهم امنیت حساب تلگرام را در یک‌جا پیدا کنید." data-en="Welcome to the official SELF BOT website. Explore project information, getting-started guidance, and important Telegram account security tips in one place.">به صفحه رسمی SELF BOT خوش آمدید. امکانات پروژه، راهنمای شروع و نکته‌های مهم امنیت حساب تلگرام را در یک‌جا پیدا کنید.</p>
<div class="buttons">
<a href="#features" class="btn primary" data-fa="مشاهده امکانات ←" data-en="Explore Features →">مشاهده امکانات ←</a>
<a href="#guide" class="btn secondary" data-fa="راهنمای شروع" data-en="Getting Started">راهنمای شروع</a>
</div>
</section>

<section class="section" id="features">
<div class="section-title">
<h2 data-fa="امکانات ویب‌سایت" data-en="Website Features">امکانات ویب‌سایت</h2>
<p data-fa="همه اطلاعات مهم پروژه در یک‌جا" data-en="Everything important about the project in one place">همه اطلاعات مهم پروژه در یک‌جا</p>
</div>
<div class="grid">
<div class="box"><div class="icon">🤖</div><h3 data-fa="معرفی سلف‌بات" data-en="About the Self Bot">معرفی سلف‌بات</h3><p data-fa="با پروژه SELF BOT و هدف آن آشنا شوید." data-en="Learn about the SELF BOT project and its purpose.">با پروژه SELF BOT و هدف آن آشنا شوید.</p></div>
<div class="box"><div class="icon">⚙️</div><h3 data-fa="راهنمای استفاده" data-en="Usage Guide">راهنمای استفاده</h3><p data-fa="راهنمای شروع کار و اطلاعات لازم برای استفاده از پروژه." data-en="Find introductory guidance and information for using the project.">راهنمای شروع کار و اطلاعات لازم برای استفاده از پروژه.</p></div>
<div class="box"><div class="icon">🌐</div><h3 data-fa="دری و انگلیسی" data-en="Dari and English">دری و انگلیسی</h3><p data-fa="زبان صفحه را با یک کلیک تغییر دهید." data-en="Switch the website language with one click.">زبان صفحه را با یک کلیک تغییر دهید.</p></div>
<div class="box"><div class="icon">🔐</div><h3 data-fa="امنیت حساب" data-en="Account Security">امنیت حساب</h3><p data-fa="نکته‌های مهم برای محافظت از حساب و اطلاعات شخصی." data-en="Important tips for protecting your account and personal information.">نکته‌های مهم برای محافظت از حساب و اطلاعات شخصی.</p></div>
<div class="box"><div class="icon">📱</div><h3 data-fa="مناسب موبایل" data-en="Mobile Friendly">مناسب موبایل</h3><p data-fa="طراحی سازگار با تلفن همراه، تبلت و کمپیوتر." data-en="Designed for phones, tablets, and desktop computers.">طراحی سازگار با تلفن همراه، تبلت و کمپیوتر.</p></div>
<div class="box"><div class="icon">🧭</div><h3 data-fa="دسترسی آسان" data-en="Easy Navigation">دسترسی آسان</h3><p data-fa="بخش‌های مرتب برای یافتن سریع اطلاعات." data-en="Organized sections help you find information quickly.">بخش‌های مرتب برای یافتن سریع اطلاعات.</p></div>
</div>
</section>

<section class="section" id="guide">
<div class="section-title">
<h2 data-fa="راهنمای شروع" data-en="Getting Started">راهنمای شروع</h2>
<p data-fa="برای شروع این مراحل را دنبال کنید" data-en="Follow these steps to get started">برای شروع این مراحل را دنبال کنید</p>
</div>
<div class="steps">
<div class="step"><strong data-fa="اطلاعات پروژه را بخوانید" data-en="Read about the project">اطلاعات پروژه را بخوانید</strong><div data-fa="ابتدا امکانات و توضیحات پروژه را بررسی کنید." data-en="First, review the project information and features.">ابتدا امکانات و توضیحات پروژه را بررسی کنید.</div></div>
<div class="step"><strong data-fa="راهنمای رسمی را دنبال کنید" data-en="Follow official guidance">راهنمای رسمی را دنبال کنید</strong><div data-fa="برای راه‌اندازی، فقط از راهنمای معتبر و منابع رسمی استفاده کنید." data-en="Use trusted instructions and official resources when setting things up.">برای راه‌اندازی، فقط از راهنمای معتبر و منابع رسمی استفاده کنید.</div></div>
<div class="step"><strong data-fa="حساب خود را امن نگه دارید" data-en="Keep your account secure">حساب خود را امن نگه دارید</strong><div data-fa="کد ورود، رمز دومرحله‌ای و فایل نشست خود را با دیگران شریک نسازید." data-en="Never share your login code, two-step verification password, or session file.">کد ورود، رمز دومرحله‌ای و فایل نشست خود را با دیگران شریک نسازید.</div></div>
</div>
</section>

<section class="section" id="security">
<div class="notice">
<strong data-fa="🛡️ نکته مهم امنیتی" data-en="🛡️ Important Security Notice">🛡️ نکته مهم امنیتی</strong>
<span data-fa="این ویب‌سایت برای معرفی پروژه و ارائه راهنما است؛ در آن کد ورود تلگرام، رمز دومرحله‌ای یا فایل نشست خود را وارد نکنید. اتصال حساب باید از راهی امن انجام شود و اطلاعات محرمانه نباید در ویب‌سایت جمع‌آوری یا ذخیره شود." data-en="This website provides project information and guidance. Do not enter your Telegram login code, two-step verification password, or session file here. Account linking must use a secure method, and confidential credentials should not be collected or stored by this website.">این ویب‌سایت برای معرفی پروژه و ارائه راهنما است؛ در آن کد ورود تلگرام، رمز دومرحله‌ای یا فایل نشست خود را وارد نکنید. اتصال حساب باید از راهی امن انجام شود و اطلاعات محرمانه نباید در ویب‌سایت جمع‌آوری یا ذخیره شود.</span>
</div>
</section>

<section class="section faq" id="faq">
<div class="section-title"><h2 data-fa="پرسش‌های متداول" data-en="Frequently Asked Questions">پرسش‌های متداول</h2></div>
<details><summary data-fa="آیا ویب‌سایت رمز یا کود تلگرام را می‌گیرد؟" data-en="Does the website ask for Telegram codes or passwords?">آیا ویب‌سایت رمز یا کود تلگرام را می‌گیرد؟</summary><p data-fa="خیر. این صفحه برای معرفی و راهنمایی است و نباید اطلاعات محرمانه حساب را وارد کنید." data-en="No. This page is for information and guidance. Do not enter confidential account details here.">خیر. این صفحه برای معرفی و راهنمایی است و نباید اطلاعات محرمانه حساب را وارد کنید.</p></details>
<details><summary data-fa="آیا صفحه در موبایل کار می‌کند؟" data-en="Does the website work on mobile?">آیا صفحه در موبایل کار می‌کند؟</summary><p data-fa="بلی، طراحی صفحه با موبایل و کمپیوتر سازگار است." data-en="Yes, the design supports mobile phones and desktop computers.">بلی، طراحی صفحه با موبایل و کمپیوتر سازگار است.</p></details>
<details><summary data-fa="چگونه زبان صفحه را تغییر بدهم؟" data-en="How do I change the language?">چگونه زبان صفحه را تغییر بدهم؟</summary><p data-fa="روی دکمه EN / دری در بالای صفحه بزنید." data-en="Tap the EN / دری button at the top of the page.">روی دکمه EN / دری در بالای صفحه بزنید.</p></details>
</section>

<section class="section contact" id="contact">
<h2 data-fa="تیم SELF BOT" data-en="The SELF BOT Team">تیم SELF BOT</h2>
<p data-fa="ساخته‌شده با تلاش تیم انیل و توفیق" data-en="Built with the efforts of the Anil and Tawfiq team">ساخته‌شده با تلاش تیم انیل و توفیق</p>
<a class="btn secondary" href="https://telegram.org/" target="_blank" rel="noopener noreferrer" data-fa="وب‌سایت رسمی تلگرام ↗" data-en="Official Telegram Website ↗">وب‌سایت رسمی تلگرام ↗</a>
</section>
</main>

<footer>
<div><span>SELF BOT</span> • ANIL AND TAWFIQ</div>
<div data-fa="© تمام حقوق محفوظ است" data-en="© All rights reserved">© تمام حقوق محفوظ است</div>
</footer>
<script>
let currentLang="fa";
function toggleLang(){
 currentLang=currentLang==="fa"?"en":"fa";
 document.documentElement.lang=currentLang;
 document.documentElement.dir=currentLang==="fa"?"rtl":"ltr";
 document.querySelectorAll("[data-fa]").forEach(el=>{
   const value=el.getAttribute("data-"+currentLang);
   if(value!==null) el.textContent=value;
 });
}
</script>
</body>
</html>
""")
