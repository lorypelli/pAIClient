from os.path import isdir

from fastapi import Request
from fastapi.responses import FileResponse, RedirectResponse
from utils.client import gpt


def frontend(req: Request, path: str):
    path = path.replace("index.html", "")
    d = "../frontend/dist"
    token = req.cookies.get("token")
    if token and token.strip() != "":
        try:
            gpt.api_key = token
            gpt.models.list()
        except:
            res = RedirectResponse("/login", 302)
            res.delete_cookie("token")
            return res
    if path != "login" and isdir(f"{d}/{path}") and not req.cookies.get("token"):
        return RedirectResponse("/login", 302)
    if path == "login" and req.cookies.get("token"):
        return RedirectResponse("/", 302)
    if isdir(f"{d}/{path}"):
        path = f"{path}/index.html"
    res = FileResponse(f"{d}/{path}")
    res.delete_cookie("messages")
    return res
