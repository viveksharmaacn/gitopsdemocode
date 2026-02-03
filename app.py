from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! from Vivek !!!!! Welcome to GitOps World !!!!"
