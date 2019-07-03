from flask import Flask, make_response

from user import userApp;

app = Flask(__name__)

@app.route("/")
def hello_path():
  return make_response("Hello, world"), 200


app.register_blueprint(userApp, url_prefix="/user")