from fastapi import APIRouter
from routes.config import get_config, post_config
from routes.env import env
from routes.error import error
from routes.frontend import frontend
from routes.login import login
from routes.response import response

router = APIRouter()

router.add_api_route("/api/config", get_config, methods=["GET"])
router.add_api_route("/api/config", post_config, methods=["POST"])
router.add_api_route("/api/env", env, methods=["GET"])
router.add_api_route("/api/login", login, methods=["POST"])
router.add_api_route("/api/response", response, methods=["POST"])

router.add_api_route("/{path:path}", frontend, methods=["GET", "POST"])
