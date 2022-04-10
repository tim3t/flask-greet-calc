# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div


app = Flask(__name__)

# PART ONE
# @app.route('/add')
# def q_add():
#     a=int(request.args.get("a"))
#     b=int(request.args.get("b"))
#     result = add(a,b)
#     return str(result)

# @app.route('/subtract')
# def q_subtract():
#     a=int(request.args.get("a"))
#     b=int(request.args.get("b"))
#     result = sub(a,b)
#     return str(result)

# @app.route('/multiply')
# def q_multiply():
#     a=int(request.args.get("a"))
#     b=int(request.args.get("b"))
#     result = mult(a,b)
#     return str(result)

# @app.route('/divide')
# def q_divide():
#     a=int(request.args.get("a"))
#     b=int(request.args.get("b"))
#     result = div(a,b)
#     return str(result)

# PART TWO
operators= {
    "add": add,
    "subtract": sub,
    "multiply": mult,
    "divide": div
}
@app.route('/<operator>')
def q_math(operator):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[operator](a,b)
    return str(result)