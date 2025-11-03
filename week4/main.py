# Task 1
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Task 2
from typing import Annotated
from fastapi import Form, status
from fastapi.responses import RedirectResponse

# Task 3
from starlette.middleware.sessions import SessionMiddleware
import secrets

# Task 4
import urllib.request as request
import json

SESSION_KEY = "LOGGED-IN"
secret_key = secrets.token_urlsafe(32)

from contextlib import asynccontextmanager


# The code inside lifespan is guaranteed to run after the application object is created and
# before the server starts processing its first request.
# This is the correct moment to finalize setup
@asynccontextmanager
async def lifespan(app: FastAPI):
    fetch_and_load_hotel_data()
    yield


app = FastAPI(lifespan=lifespan)
app.add_middleware(SessionMiddleware, secret_key=secret_key)
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/login/")
async def login(
    request: Request, email: Annotated[str, Form()], password: Annotated[str, Form()]
):
    if not email or not password:
        return RedirectResponse(
            url="/ohoh?msg=請輸入信箱和密碼", status_code=status.HTTP_303_SEE_OTHER
        )

    if email == "abc@abc.com" and password == "abc":
        request.session[SESSION_KEY] = True
        return RedirectResponse(url="/member", status_code=status.HTTP_303_SEE_OTHER)

    else:
        return RedirectResponse(
            url="/ohoh?msg=信箱或密碼輸入錯誤", status_code=status.HTTP_303_SEE_OTHER
        )


@app.get("/member", response_class=HTMLResponse)
async def member_page(request: Request):
    if SESSION_KEY not in request.session or not request.session[SESSION_KEY]:
        return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
    return templates.TemplateResponse("member.html", {"request": request})


@app.get("/ohoh", response_class=HTMLResponse)
async def error_page(request: Request, msg: str):
    return templates.TemplateResponse("ohoh.html", {"request": request, "msg": msg})


@app.get("/logout", response_class=HTMLResponse)
async def logout(request: Request):
    request.session[SESSION_KEY] = False
    return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)


@app.get("/hotel/{id}")
async def get_hotel_data(request: Request, id: int):
    hotel_data = request.app.state.hotel_data
    if id in hotel_data:
        return templates.TemplateResponse(
            "hotel.html", {"request": request, "hotel_info": hotel_data[id]}
        )
    else:
        return templates.TemplateResponse("hotel.html", {"request": request})


CH_HOTEL_URL = "https://resources-wehelp-taiwan-b986132eca78c0b5eeb736fc03240c2ff8b7116.gitlab.io/hotels-ch"
EN_HOTEL_URL = "https://resources-wehelp-taiwan-b986132eca78c0b5eeb736fc03240c2ff8b7116.gitlab.io/hotels-en"


def fetch_and_load_hotel_data():

    with request.urlopen(CH_HOTEL_URL) as response:
        ch_data = json.load(response)

    with request.urlopen(EN_HOTEL_URL) as response:
        en_data = json.load(response)

    ch_hotel_list = ch_data["list"]
    en_hotel_list = en_data["list"]
    merged_hotel_list = []

    hotel_id_lookup = {hotel["_id"]: hotel for hotel in ch_hotel_list}

    # Merge English names into Chinese data
    for hotel in en_hotel_list:
        _id = hotel["_id"]
        if _id in hotel_id_lookup:
            merged_hotel = {**hotel_id_lookup[_id], **hotel}
            merged_hotel_list.append(merged_hotel)

    hotel_data = {hotel["_id"]: hotel for hotel in merged_hotel_list}
    # Store the data on the application state
    app.state.hotel_data = hotel_data
