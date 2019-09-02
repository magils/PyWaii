from flask import Flask
import os


def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='MySecretKey',
        DATABASE=os.path.join(app.instance_path,'flaskr.sqlite')
    )

    if not test_config:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/dummy")
    def dummy():
        return "This is dummy"

    from . import db

    db.init_app(app)

    from . import auth

    app.register_blueprint(auth.auth_bp)

    return app


