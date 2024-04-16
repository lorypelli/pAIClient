from fastapi import FastAPI
from fastapi.responses import FileResponse
from uvicorn import run
from os.path import isdir
app = FastAPI()
@app.get('/{path:path}')
def frontend(path: str):
    d = '../frontend/dist'
    if isdir(f'{d}/{path}'):
        path = f'{path}/index.html'
    return FileResponse(f'{d}/{path}')
if __name__ == '__main__':
    run('main:app', port=5173, reload=True)