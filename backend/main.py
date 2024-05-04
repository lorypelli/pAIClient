from fastapi import FastAPI, Request, Response
from fastapi.responses import FileResponse, RedirectResponse, JSONResponse, StreamingResponse
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
                res.set_cookie('model', model, max_age=int(timedelta(90).total_seconds()), secure=True, httponly=True)
            prompt = body.get('prompt')
            if prompt and prompt.strip() != '':
                res.set_cookie('prompt', prompt, max_age=int(timedelta(90).total_seconds()), secure=True, httponly=True)
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
            try:
                openai.api_key = token
                openai.models.list()
            except:
                return RedirectResponse('/login')
            res.set_cookie('token', token, max_age=int(timedelta(21).total_seconds()), secure=True, httponly=True)
            res.set_cookie('model', 'gpt-3.5-turbo', max_age=int(timedelta(90).total_seconds()), secure=True, httponly=True)
            res.set_cookie('prompt', '', max_age=int(timedelta(90).total_seconds()), secure=True, httponly=True)
        return res
    except:
        return Response('Body is not a valid JSON with token property', 400)
def openai_response(model: str, messages: list):
    try:
        res = openai.chat.completions.create(temperature=0.0, model=model, messages=messages, stream=True)
        try:
            for c in res:
                if c.choices[0].delta.content:
                    yield c.choices[0].delta.content
        except:
            raise Exception('There was an error')
    except:
        raise Exception('There was an error')
@app.post('/api/response')
async def response(req: Request):
    token = req.cookies.get('token')
    if token and token.strip() != '':
        openai.api_key = token
        try:
            body = await req.json()
            message = body.get('message')
            messages = [{ 'role': 'system', 'content': req.cookies.get('prompt') or '' }]
            if message and message.strip() != '':
                messages.append({ 'role': 'user', 'content': message })
            try:
                return StreamingResponse(openai_response(req.cookies.get('model') or 'gpt-3.5-turbo', messages))
            except:
                return Response('There was an error', 400)
        except:
            return Response('Body is not a valid JSON with message property', 400)   
@app.get('/api/download')
@app.post('/api/download')
async def download(req: Request):
    if req.method == 'GET':
        messages = req.cookies.get('messages')
        if messages:
            return JSONResponse({
                'model': req.cookies.get('model') or 'gpt-3.5-turbo',
                'prompt': req.cookies.get('prompt') or '',
                'messages': messages    
            })
    elif req.method == 'POST':
        try:
            body = await req.json()
            messages = body.get('messages')
            if messages:
                res: Response = Response('Successfully set messages')
                res.set_cookie('messages', messages)
                return res
        except:
            return Response('Body is not a valid JSON with messages property', 400)
@app.get('/{path:path}')
def frontend(req: Request, path: str):
    path = path.replace('index.html', '')
    d = '../frontend/dist'
    token = req.cookies.get('token')
    if token and token.strip() != '':
        try:
            openai.api_key = token
            openai.models.list()
        except:
            res = RedirectResponse('/login')
            res.delete_cookie('token')
            return res
    if path != 'login' and isdir(f'{d}/{path}') and not req.cookies.get('token'):
        return RedirectResponse('/login')
    if path == 'login' and req.cookies.get('token'):
        return RedirectResponse('/')
    if path != 'login' and isdir(f'{d}/{path}') and not req.cookies.get('token'):
        return RedirectResponse('/login')
    if isdir(f'{d}/{path}'):
        path = f'{path}/index.html'
    res: FileResponse = FileResponse(f'{d}/{path}')
    res.delete_cookie('messages')
    return res
@app.exception_handler(500)
def error(*args):
    return RedirectResponse('/')
if __name__ == '__main__':
    run('main:app', port=5173, reload=True)