from fastapi.responses import RedirectResponse


def error(*args):
    return RedirectResponse("/", 302)
