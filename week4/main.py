# Task 1
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


# Task 2
from typing import Annotated
from fastapi import Form, status
from fastapi.responses import RedirectResponse


@app.post("/login/")
async def login(email: Annotated[str, Form()], password: Annotated[str, Form()]):
    if not email or not password:
        return RedirectResponse(
            url="/ohoh?msg=請輸入信箱和密碼", status_code=status.HTTP_303_SEE_OTHER
        )

    if email == "abc@abc.com" and password == "abc":
        return RedirectResponse(url="/member", status_code=status.HTTP_303_SEE_OTHER)

    else:
        return RedirectResponse(
            url="/ohoh?msg=信箱或密碼輸入錯誤", status_code=status.HTTP_303_SEE_OTHER
        )


@app.get("/member", response_class=HTMLResponse)
async def member_page(request: Request):
    return templates.TemplateResponse("member.html", {"request": request})


@app.get("/ohoh", response_class=HTMLResponse)
async def error_page(request: Request, msg: str):
    return templates.TemplateResponse("ohoh.html", {"request": request, "msg": msg})
