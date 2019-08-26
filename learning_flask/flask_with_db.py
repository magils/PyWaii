from flask import Flask, request, Response, jsonify
from flask_sqlalchemy import SQLAlchemy
import enum
from sqlalchemy import DateTime, Enum

from utils import CustomJsonEncoder

app = Flask(__name__)
# This DB address is because the database is running in a container
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://flask:Flask@0.0.0.0:3307/employees?charset=utf8mb4"
app.json_encoder = CustomJsonEncoder

db = SQLAlchemy(app)


# Entities definition

class Gender(enum.Enum):
    M = "M"
    F = "F"


class Employee(db.Model):
    __tablename__ = "employees"

    id = db.Column("emp_no", db.Integer, primary_key=True)
    first_name = db.Column("first_name", db.String)
    last_name = db.Column("last_name", db.String)
    gender = db.Column("gender", Enum(Gender), nullable=False)
    hire_date = db.Column("hire_date", DateTime, nullable=False)


# Employee Data Access Methods
def find_all_employees():
    return db.session.query(Employee).all()


def find_employee(employee_id):
    return db.session.query(Employee).filter_by(id=employee_id).one_or_none()


def save_employee(employee):
    db.session.add(employee)
    db.session.commit()


def delete_employee(employee_id):
    db.session.query(Employee).filter_by(id=employee_id).delete()
    db.session.commit()


def update_employee_first_name(employee_id, fist_name):
    to_update = db.session.query(Employee).filter_by(id=employee_id).one_or_none()

    if not to_update:
        return

    to_update.fist_name = fist_name
    db.session.commit()


def update_employee_lastname(employee_id, last_name):
    to_update = db.session.query(Employee).filter_by(id=employee_id)

    if not to_update:
        return

    to_update.last_name = last_name
    db.session.commit()


# Endpoint definition

@app.route("/employee")
def get_employee():
    employee_id = request.args.get("id")

    if not employee_id:
        return Response(status=400)

    employee = find_employee(employee_id)

    if not employee:
        return Response(status=404)

    return jsonify(employee)


@app.route("/employees")
def get_employees():
    employees = find_all_employees()

    return jsonify(employees)


@app.route("/employees", methods=["POST"])
def create_employee():
    employee_payload = request.get_json()

    if not employee_payload:
        return Response("Invalid JSON content",status=400)

    employee_data = employee_payload["employee"]

    new_employee = Employee()
    new_employee.first_name = employee_data["first_name"]
    new_employee.last_name = employee_data["last_name"]
    new_employee.gender = employee_data["gender"]

    save_employee(new_employee)

    return Response(new_employee,status=201)

