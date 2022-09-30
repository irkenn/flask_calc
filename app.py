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