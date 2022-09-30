from crypt import methods
from inspect import ArgSpec
from flask import Flask, request
app = Flask(__name__)# Put your app in here.

@app.route('/add')
def add():
    """Adds a and b"""
    a = request.args.get("a", type=int)
    b = request.args.get("b", type=int)
    output = a+b
    output = str(output)
    return output

@app.route('/sub')
def sub():
    """Adds a and b"""
    a = request.args.get("a", type=int)
    b = request.args.get("b", type=int)
    output = a-b
    output = str(output)
    return output

@app.route('/mult')
def mult():
    """Adds a and b"""
    a = request.args.get("a", type=int)
    b = request.args.get("b", type=int)
    output = a*b
    output = str(output)
    return output

@app.route('/div')
def div():
    """Adds a and b"""
    a = request.args.get("a", type=int)
    b = request.args.get("b", type=int)
    output = a/b
    output = str(output)
    return output

operators = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }

@app.route("/math/<oper>")
def do_math(oper):
    """Do math on a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[oper](a, b)

    return str(result) 