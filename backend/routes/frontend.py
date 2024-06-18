from os.path import isdir

from fastapi import Request
from fastapi.responses import FileResponse, HTMLResponse, RedirectResponse
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
            res = RedirectResponse("/login")
            res.delete_cookie("token")
            return res
    if path != "login" and isdir(f"{d}/{path}") and not req.cookies.get("token"):
        return RedirectResponse("/login")
    if path == "login" and req.cookies.get("token"):
        return RedirectResponse("/")
    if isdir(f"{d}/{path}"):
        path = f"{path}/index.html"
    with open(f"{d}/{path}") as f:
        html_content = f.read()
        html_content = html_content.replace(
            "</head>",
            f"""<script>
            window.token='{req.cookies.get('token') or ''}'
            window.config={{ model: '{req.cookies.get('model') or 'gpt-3.5-turbo'}', prompt: '{req.cookies.get('prompt') or ''}' }}
            </script>
            </head>""",
        )
    res: FileResponse | HTMLResponse = FileResponse(f"{d}/{path}")
    if path.endswith(".html"):
        res = HTMLResponse(html_content)
    res.delete_cookie("messages")
    return res
