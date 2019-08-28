import datetime
from flask import Flask, request, Response, jsonify, Blueprint
import enum

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime, Enum
from learning_flask import create_app

app = create_app(__name__)
db = SQLAlchemy(app)

class Gender(enum.Enum):
    M = "M"
    F = "F"


class Employee(db.Model):
    __tablename__ = "employees"

    id = db.Column("emp_no", db.Integer, primary_key=True)
    first_name = db.Column("first_name", db.String)
    last_name = db.Column("last_name", db.String)
    gender = db.Column("gender", Enum(Gender), nullable=False)
    hire_date = db.Column(
        "hire_date", DateTime, nullable=False, default=datetime.date.today()
    )
    birth_date = db.Column("birth_date", DateTime, nullable=False)


# Declaring BluePrint for employees endpoints

employee_blueprint = Blueprint("employee", __name__, url_prefix="/employee")
app.register_blueprint(employee_blueprint)

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

    try:

        employee_data = employee_payload["employee"]

        new_employee = Employee()
        new_employee.first_name = employee_data["first_name"]
        new_employee.last_name = employee_data["last_name"]
        new_employee.gender = employee_data["gender"]
        new_employee.birth_date = datetime.date.today()

        save_employee(new_employee)

        return jsonify(new_employee)

    except KeyError:
        return Response("Invalid JSON content", status=400)


@employee_blueprint.route("/test")
def blueprint_demo():
    return Response("This is a demo")
