#!/usr/bin/env python3
"""
Auth module for the API
"""
from flask import request
from typing import List, TypeVar


class Auth():
    """ Auth Class """
    def __init__(self):
        """ initialize the auth class """
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ blank """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        
        for paths in excluded_paths:
            if path.rstrip('/') in paths.rstrip('/'):
                return False
        
        return True

    def authorization_header(self, request=None) -> str:
        """ blank """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ blank """
        return None
