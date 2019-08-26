from flask.json import JSONEncoder
import flask_with_db


class CustomJsonEncoder(JSONEncoder):

    def default(self,obj):

        if isinstance(obj,flask_with_db.Employee):

            employee_dict = {
                "id": obj.id,
                "first_name": obj.first_name,
                "last_name": obj.last_name,
                "gender": obj.gender.value,
                "hire_date": obj.hire_date
            }

            return employee_dict

        return super(CustomJsonEncoder, self).default(obj)



