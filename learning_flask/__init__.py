from flask import Flask
from utils import CustomJsonEncoder

def create_app(name):
    app = Flask(name)
    # This DB address is because the database is running in a container
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://flask:Flask@0.0.0.0:3307/employees?charset=utf8mb4"
    app.json_encoder = CustomJsonEncoder

    return app


