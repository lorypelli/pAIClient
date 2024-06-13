from fastapi import Request
from fastapi.responses import PlainTextResponse


def token(req: Request):
    return PlainTextResponse(req.cookies.get("token") or "")
