# Task 1
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Task 2
from typing import Annotated
from fastapi import Form, status
from dotenv import load_dotenv
from fastapi.responses import RedirectResponse
import os
import mysql.connector

# Task 3
from starlette.middleware.sessions import SessionMiddleware
import secrets

load_dotenv()


mysql_user = os.getenv("MYSQL_USER")
mysql_password = os.getenv("MYSQL_PASSWORD")

secret_key = secrets.token_urlsafe(32)

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=secret_key)
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


def get_website_db_connection():
    return mysql.connector.connect(
        user=mysql_user, password=mysql_password, host="localhost", database="website"
    )


@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/signup")
async def signup(
    request: Request,
    signup_name: Annotated[str, Form()],
    signup_email: Annotated[str, Form()],
    signup_password: Annotated[str, Form()],
):
    db = get_website_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM member WHERE email=%s;", (signup_email,))
    email_exists = cursor.fetchone()

    if email_exists:
        db.close()
        return RedirectResponse(
            url="/ohoh?msg=重複的電子郵件", status_code=status.HTTP_303_SEE_OTHER
        )

    cursor.execute(
        "INSERT INTO member (name, email, password) VALUES (%s, %s, %s);",
        (signup_name, signup_email, signup_password),
    )
    db.commit()
    db.close()
    return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)


@app.post("/login")
async def login(
    request: Request,
    login_email: Annotated[str, Form()],
    login_password: Annotated[str, Form()],
):
    db = get_website_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute(
        "SELECT * FROM member WHERE email=%s AND password=%s;",
        (login_email, login_password),
    )
    user = cursor.fetchone()  # type: ignore
    db.close()

    if user:
        request.session["LOGGED-IN"] = {
            "user_name": user["name"],
            "user_email": user["email"],
            "user_id": str(user["id"]),
        }
        return RedirectResponse(url="/member", status_code=status.HTTP_303_SEE_OTHER)
    else:
        return RedirectResponse(
            url="/ohoh?msg=電子郵件或密碼錯誤", status_code=status.HTTP_303_SEE_OTHER
        )


@app.get("/logout", response_class=HTMLResponse)
async def logout(request: Request):
    request.session["LOGGED-IN"] = False
    return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)


@app.get("/member", response_class=HTMLResponse)
async def member_page(request: Request):
    if "LOGGED-IN" not in request.session or not request.session["LOGGED-IN"]:
        return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
    return templates.TemplateResponse("member.html", {"request": request})


@app.get("/ohoh", response_class=HTMLResponse)
async def error_page(request: Request, msg: str):
    return templates.TemplateResponse("ohoh.html", {"request": request, "msg": msg})
