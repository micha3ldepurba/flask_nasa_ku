from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Deploy sukses, tapi masih dummy!"
