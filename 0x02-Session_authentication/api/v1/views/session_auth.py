#!/usr/bin/env python3
"""New view for Session Authentication"""
from api.v1.views import session_views
from flask import jsonify, request, make_response
from models.user import User
import os


@session_views.route('/auth_session/login', methods=['POST'],
                     strict_slashes=False)
def session_login() -> dict:
    """Handles user login and session creation."""
    email = request.form.get('email')
    if email is None:
        return jsonify({"error": "email missing"}), 400

    password = request.form.get('password')
    if password is None:
        return jsonify({"error": "password missing"}), 400

    users = User.search({"email": email})
    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    for user in users:
        if user.is_valid_password(password):
            from api.v1.app import auth  # import auth
            user_id = user.id  # or user.get('id') if applicable
            session_id = auth.create_session(user_id)
            user_dict = user.to_json()
            session_name = os.getenv('SESSION_NAME', '_my_session_id')
            response = make_response(jsonify(user_dict))
            response.set_cookie(session_name, session_id)
            return response

    return jsonify({"error": "wrong password"}), 401
