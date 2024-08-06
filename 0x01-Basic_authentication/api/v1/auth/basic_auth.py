#!/usr/bin/env python3
"""This module implements BasicAuth class"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """The BasicAuth class"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str
                                            ) -> str:
        """Returns the Base64 part of the Authorization header for a
        Basic Authentication"""
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith('Basic '):
            return None

        return authorization_header.lstrip('Basic ')
