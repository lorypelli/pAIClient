from typing import Annotated

from fastapi import Depends, Request
from fastapi.responses import RedirectResponse, StreamingResponse
from fastapi.security import APIKeyHeader
from utils.client import gpt
from utils.response import openai_response

auth = APIKeyHeader(name="Authorization")


async def response(token: Annotated[str, Depends(auth)], req: Request):
    try:
        gpt.api_key = token
        gpt.models.list()
        body = await req.json()
        message = body.get("message")
        messages = [{"role": "system", "content": req.cookies.get("prompt") or ""}]
        if message and message.strip() != "":
            messages.append({"role": "user", "content": message})
        return StreamingResponse(
            openai_response(req.cookies.get("model") or "gpt-3.5-turbo", messages)
        )
    except:
        return RedirectResponse("/login")
