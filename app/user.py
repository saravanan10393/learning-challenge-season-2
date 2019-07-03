from flask import Blueprint, request, jsonify;

userApp = Blueprint('User', __name__);


def add_user():
  print("create user details ===> %s", request.form)
  return jsonify({"name": "sara"})


def update_user(user_id):
  print("update user details ===> %s", request.form)
  return jsonify({"name": "sara"})

userApp.add_url_rule('/', endpoint='add_user', view_func=add_user, methods=["POST"])
userApp.add_url_rule('/<user_id>/update', endpoint='update_user', view_func=update_user, methods=["POST"])