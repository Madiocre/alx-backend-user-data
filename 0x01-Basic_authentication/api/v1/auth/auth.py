#!/usr/bin/env python3
"""
Auth module for the API
"""
from api.v1.views import app_views
from flask import request
from typing import List, TypeVar


class Auth:
    """ """
    def __init__(self):
        """ initialize the auth class """
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ """
        return False

    def authorization_header(self, request=None) -> str:
        """ """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ """
        return None
