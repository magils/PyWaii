from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from utils import CustomJsonEncoder

app = Flask(__name__)
# This DB address is because the database is running in a container
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://flask:Flask@0.0.0.0:3307/employees?charset=utf8mb4"
app.json_encoder = CustomJsonEncoder

db = SQLAlchemy(app)

