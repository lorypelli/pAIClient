from fastapi import Request
from fastapi.responses import Response


def token(req: Request):
    return Response(req.cookies.get("token") or "")
