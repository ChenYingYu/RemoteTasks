from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/member", response_class=HTMLResponse)
async def member_page(request: Request):
    return templates.TemplateResponse("member.html", {"request": request})


@app.get("/ohoh", response_class=HTMLResponse)
async def error_page(request: Request):
    return templates.TemplateResponse(
        "ohoh.html", {"request": request, "msg": "帳號、或密碼輸入錯誤"}
    )
