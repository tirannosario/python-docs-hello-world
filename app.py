from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/<user>")
def show_user(user):
    return "Hello %s from Rosario :)" % user
