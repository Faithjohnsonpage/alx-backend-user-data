#!/usr/bin/env python3
"""This module handles authentification"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers the user"""
        if email is None or password is None:
            raise ValueError("Email and password cannot be None")

        try:
            self._db.find_user_by(email=email)
            raise ValueError(f'User {email} already exists')
        except NoResultFound:
            hashed_password = _hash_password(password)
            return self._db.add_user(email, hashed_password)          


def _hash_password(password: str) -> bytes:
    """Hash the password"""
    bytes = password.encode()
    return bcrypt.hashpw(bytes, bcrypt.gensalt())
