from os import getenv

from dotenv import load_dotenv
from fastapi.responses import PlainTextResponse


def env():
    load_dotenv()
    return PlainTextResponse(getenv("OPENAI_API_KEY", ""))
