#!/usr/bin/env python3
"""
Auth module for the API
"""
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth
import re


class BasicAuth(Auth):
    """ Auth Class """
    def __init__(self):
        """ initialize the auth class """
        pass

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ returns the Base64 part of the Authorization header
        for a Basic Authentication
        """
        if not authorization_header:
            return None
        if not isinstance(authorization_header, str):
            return None

        match = re.match(r'^Basic ', authorization_header)
        if not match:
            return None

        return authorization_header[len(match.group(0)):]
