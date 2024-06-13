from datetime import timedelta

from fastapi import Form, Request
from fastapi.responses import JSONResponse, RedirectResponse


def get_config(req: Request):
    return JSONResponse(
        {
            "model": req.cookies.get("model") or "gpt-3.5-turbo",
            "prompt": req.cookies.get("prompt") or "",
        }
    )


def post_config(model: str = Form(), prompt: str = Form("")):
    res: Response = RedirectResponse("/")
    if model and model.strip() != "":
        res.set_cookie(
            "model",
            model,
            max_age=int(timedelta(90).total_seconds()),
            secure=True,
            httponly=True,
        )
        res.set_cookie(
            "prompt",
            prompt,
            max_age=int(timedelta(90).total_seconds()),
            secure=True,
            httponly=True,
        )
    return res
