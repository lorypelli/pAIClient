from fastapi import FastAPI
from routes import router
from routes.error import error
from utils.client import gpt
from uvicorn import run

app = FastAPI(docs_url="/api/docs", redoc_url=None)
app.include_router(router)
app.add_exception_handler(500, error)

if __name__ == "__main__":
    run("main:app", port=5173, reload=True)
