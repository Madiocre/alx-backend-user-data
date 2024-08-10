#!/usr/bin/env python3
"""
Auth module for the API
"""
from flask import request
from typing import List, TypeVar
import fnmatch
import os


class Auth():
    """ Auth Class """
    def __init__(self):
        """ initialize the auth class """
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method to check of path is excluded.
        """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True

        for paths in excluded_paths:
            if path.rstrip('/') in paths.rstrip('/*'):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Method to get authorization header.
        """
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ blank """
        return None

    def session_cookie(self, request=None):
        """
        Returns a cookie from a request
        Args:
            request : request object
        Return:
            value of _my_session_id cookie from request object
        """
        if request is None:
            return None
        session_name = os.getenv('SESSION_NAME')
        return request.cookies.get(session_name)
