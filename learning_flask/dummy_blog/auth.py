import functools

from flask import Blueprint
from dummy_blog.db import get_db

auth_bp = Blueprint("authentication", __name__, url_prefix="/auth")


@auth_bp.route("/register", methods=("GET", "POST"))
def register():
    return "This is the register page"


@auth_bp.route("/login")
def login():
    return "This is the login page"