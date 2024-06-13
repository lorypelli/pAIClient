from os.path import isdir

from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, RedirectResponse
from routes import router
from utils.client import gpt
from uvicorn import run

app = FastAPI(docs_url="/api/docs", redoc_url=None)
app.include_router(router)


@app.get("/{path:path}")
@app.post("/{path:path}")
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
    res: FileResponse = FileResponse(f"{d}/{path}")
    res.delete_cookie("messages")
    return res


@app.exception_handler(500)
def error(*args):
    return RedirectResponse("/")


if __name__ == "__main__":
    run("main:app", port=5173, reload=True)
