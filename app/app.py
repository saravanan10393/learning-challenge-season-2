from flask import Flask, make_response

app = Flask(__name__)

@app.route("/")
def hello_path():
  return make_response("Hello, world"), 200
