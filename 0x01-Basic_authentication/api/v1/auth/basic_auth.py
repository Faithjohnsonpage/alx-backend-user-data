#!/usr/bin/env python3
"""This module implements BasicAuth class"""
from api.v1.auth.auth import Auth
import base64


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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """Returns the decoded value of a Base64 string
        base64_authorization_header"""
        if base64_authorization_header is None:
            return None

        if not isinstance(base64_authorization_header, str):
            return None
        try:
            if base64_authorization_header.startswith('Basic '):
                base64_str = self.extract_base64_authorization_header(
                        base64_authorization_header)
                decoded_bytes = base64.b64decode(base64_str)

            # Decode the Base64 string
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')

        except (base64.binascii.Error, UnicodeDecodeError):
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """Returns user email and password from the Base64 decoded value"""
        if decoded_base64_authorization_header is None:
            return (None, None)

        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)

        if ':' not in decoded_base64_authorization_header:
            return (None, None)

        # Split the string into username and password
        try:
            username, password =\
                    decoded_base64_authorization_header.split(':', 1)
            return (username, password)
        except ValueError:
            return (None, None)
