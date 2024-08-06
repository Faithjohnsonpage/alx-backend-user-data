#!/usr/bin/env python3
"""API authentication"""
from flask import request
from typing import List, TypeVar


class Auth:
    """This class manages the API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if the path requires authentication"""
        if path is None:
            return True

        if excluded_paths is None or not excluded_paths:
            return True

        # Normalize the path
        path = path.rstrip('/') + '/'  # Ensure the path ends with a slash

        for excluded_path in excluded_paths:
            # Normalize the excluded path
            normalized_excluded_path = excluded_path.rstrip('/') + '/'
            if normalized_excluded_path.endswith('*'):
                # Remove the wildcard
                normalized_excluded_path = normalized_excluded_path[:-1]
                if path.startswith(normalized_excluded_path):
                    return False
            elif path.startswith(normalized_excluded_path):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """Get the authorization header from the request"""
        if request is None:
            return None

        authorization_header = request.headers.get('Authorization')
        return authorization_header if authorization_header else None

    def current_user(self, request=None) -> TypeVar('User'):
        """Get the current user from the request"""
        return None
