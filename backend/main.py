from fastapi import FastAPI, Request, Response
from fastapi.responses import FileResponse, RedirectResponse, JSONResponse
from uvicorn import run
from os.path import isdir
from datetime import datetime, timedelta
from requests import get
import openai
app = FastAPI(docs_url='/api/docs', redoc_url=None)
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
                res.set_cookie('model', model, expires=int(timedelta(30).total_seconds()), secure=True, httponly=True)
            prompt = body.get('prompt')
            if prompt and prompt.strip() != '':
                res.set_cookie('prompt', prompt, expires=int(timedelta(30).total_seconds()), secure=True, httponly=True)
            return res
        except:
            return Response('Body is not a valid JSON with model and prompt properties', 400)
@app.post('/api/login')
async def token(req: Request):
    try:
        body = await req.json()
        token = body.get('token')
        res: Response = Response('Successfully set token')
        if token and token.strip() != '':
            res.set_cookie('token', token, max_age=int(timedelta(14).total_seconds()), secure=True, httponly=True)
            res.set_cookie('model', 'gpt-3.5-turbo', max_age=int(timedelta(30).total_seconds()), secure=True)
            res.set_cookie('prompt', '', max_age=int(timedelta(30).total_seconds()), secure=True)
        return res
    except:
        return Response('Body is not a valid JSON with token property', 400)
@app.post('/api/response')
async def response(req: Request):
    try:
        body = await req.json()
        token = body.get('token')
        if token and token.strip() != '':
            openai.api_key = token
            message = body.get('message')
            messages = [{ 'role': 'system', 'content': req.cookies.get('prompt') or '' }]
            if message and message.strip() != '':
                messages.append({ 'role': 'user', 'content': message })
            try:
                res = openai.chat.completions.create(temperature=0.0, model=req.cookies.get('model') or 'gpt-3.5-turbo', messages=messages)
                return Response(res.choices[0].message.content)
            except:
                return Response('There was an error', 400)
    except:
        return Response('Body is not a valid JSON with token and message properties', 400)
@app.get('/{path:path}')
def frontend(req: Request, path: str):
    path = path.replace('index.html', '')
    if not path:
        path = '/'
    d = '../frontend/dist'
    if path == 'login' and req.cookies.get('token'):
        return RedirectResponse('/')
    if path != 'login' and isdir(f'{d}/{path}') and not req.cookies.get('token'):
        return RedirectResponse('/login')
    if isdir(f'{d}/{path}'):
        path = f'{path}/index.html'
    return FileResponse(f'{d}/{path}')
@app.exception_handler(500)
def error(*args):
    return RedirectResponse('/')
if __name__ == '__main__':
    run('main:app', port=5173, reload=True)