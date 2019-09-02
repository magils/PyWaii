import functools

from flask import \
    (Blueprint, request, redirect, url_for, render_template,flash)
from dummy_blog.db import get_db
from werkzeug.security import generate_password_hash

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/register", methods=("GET", "POST"))
def register():

    """

    - `request.form` is a dict with keys-values pair of a submitted form.

    - `generate_password_hash()` is used for create a hash of the password value.

    - `render_template()` will render a HTML page stored somewhere.

    - `url_for()` create the URL of a method in the blueprint

    - `redirect()` does a redirect response to the generate URL.

    """

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        db = get_db()
        error = None

        if not username:
            error = "Username is required"
        elif not password:
            error = "Password is required"
        elif db.execute("select id from user where username = ?", (username,)).fetchone() is not None:
            error = "User already exists"

        if not error:
            db.execute("insert into user values (?,?)",
                       (username, generate_password_hash(password))
                      )
            db.commit()
            return redirect(url_for("auth.login"))

        flash(error)

    return render_template("auth/register.html")


@auth_bp.route("/login")
def login():
    return "This is the login page"