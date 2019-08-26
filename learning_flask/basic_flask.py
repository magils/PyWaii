from flask import Flask, request,jsonify,Response
app = Flask(__name__)

"""
    Basic HTTP methods in Flask
    - GET,POST, PUT, DELETE
"""


@app.route("/flask/show/get")
def simple_get_method():
    """
    Get method implementation
    :return:
    """

    _payload = {"info": "This is sample GET method implementation"}

    return jsonify(_payload)


@app.route("/flask/show/post",methods=["POST"])
def simple_post_method():
    """
    POST method implementation
    :return:
    """

    _payload = {"info":"This is sample POST method implementation"}
    return jsonify(_payload)


@app.route("/flask/show/put", methods=["PUT"])
def sample_put_method():

    _payload = {"info": "This is a sample PUT method implementation"}

    return jsonify(_payload)


@app.route("/flask/show/delete", methods=["DELETE"])
def sample_delete_method():

    _payload = {"info": "This is a sample DELETE method implementation"}

    return jsonify(_payload)


######

@app.route("/sample/maths", methods=["POST"])
def do_math_operations():

    """
    POST Method implementation
    :return:
    """

    _json = request.get_json()
    _error_code = 400

    if _json:

        x = _json.get("x")
        y = _json.get("y")
        operation = _json.get("operator")

        if not x or not y or not operation:

            content = {"error":-1,
                        "description":"You must provide X,Y and a valid mathematical operator"}
        else:

            math_operations = {
                "+": lambda x,y: x + y,
                "-": lambda x,y: x - y,
                "*":lambda x,y: x *y,
                "/": lambda x,y: x / y
            }

            math_operation = math_operations.get(operation)

            if math_operation:

                r = math_operation(x,y)

                content = {
                    "x": _json.get("x"),
                    "y": _json.get("y"),
                    "operation": _json.get("operation"),
                    "result": r
                }

                _error_code = 200

            else:
                content = {"error":-3, "description":"Invalid math operation"}

    else:
        content = {"error":-2, "description":"You must provide a payload with x,y and mathematical operation"}

    response = jsonify(content),_error_code

    return response


@app.route("/flask/show/delete/<int:to_delete>")
def delete_data(to_delete):

    _response_payload = "{info:Object with ID %s deleted}" % to_delete
    response = Response(_response_payload)

    return response