from fastapi import FastAPI, Request, Response
from fastapi.responses import FileResponse, RedirectResponse, JSONResponse
from uvicorn import run
from os.path import isdir
app = FastAPI()
@app.get('/api/config')
@app.post('/api/config')
async def config(req: Request):
    if req.method == 'GET':
        return JSONResponse({ 'model': req.cookies.get('model') or 'gpt-3.5-turbo', 'prompt': req.cookies.get('prompt') or '' })
    elif req.method == 'POST':
        try:
            body = await req.json()
            model = body.get('model')
            res: Response = Response('Successfully set model or prompt')
            if model and model.strip() != '':
                res.set_cookie('model', model, expires=30, secure=True, httponly=True)
            prompt = body.get('prompt')
            if prompt and prompt.strip() != '':
                res.set_cookie('prompt', prompt, expires=30, secure=True, httponly=True)
            return res
        except:
            return Response('Body is not a valid JSON with model and prompt properties', 400)
@app.post('/api/login')
async def token(req: Request):
    try:
        body = await req.json()
        token = body.get('token')
        res: Response = Response('Successfully set token')
        if token:
            res.set_cookie('token', token, expires=14, secure=True, httponly=True)
        return res
    except:
        return Response('Body is not a valid JSON with token property', 400)
@app.get('/{path:path}')
def frontend(path: str):
    d = '../frontend/dist'
    if isdir(f'{d}/{path}'):
        path = f'{path}/index.html'
    return FileResponse(f'{d}/{path}')
@app.exception_handler(500)
def error(*args):
    return RedirectResponse('/')
if __name__ == '__main__':
    run('main:app', port=5173, reload=True)