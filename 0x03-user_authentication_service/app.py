#!/usr/bin/env python3
"""This module handles the Flask application"""
from flask import Flask, jsonify, request
from auth import Auth
from sqlalchemy.orm.exc import NoResultFound


app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=["GET"], strict_slashes=False)
def message():
    """Returns the jsonified dict"""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def users():
    """Users endpoint"""
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError as e:
        return jsonify({"message": "email already registered"}), 400
        


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
