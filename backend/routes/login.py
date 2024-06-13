from datetime import timedelta

from fastapi import Form, Request
from fastapi.responses import RedirectResponse
from utils.client import gpt


def login(token: str = Form()):
    res: Response = RedirectResponse("/")
    try:
        gpt.api_key = token
        gpt.models.list()
    except:
        return RedirectResponse("/login")
    res.set_cookie(
        "token",
        token,
        max_age=int(timedelta(21).total_seconds()),
        secure=True,
        httponly=True,
    )
    res.set_cookie(
        "model",
        "gpt-3.5-turbo",
        max_age=int(timedelta(90).total_seconds()),
        secure=True,
        httponly=True,
    )
    res.set_cookie(
        "prompt",
        "",
        max_age=int(timedelta(90).total_seconds()),
        secure=True,
        httponly=True,
    )
    return res
