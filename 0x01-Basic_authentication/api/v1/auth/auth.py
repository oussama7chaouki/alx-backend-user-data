from flask import request
from typing import List, TypeVar


User = TypeVar('User')


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        # path and excluded_paths will be used later
        # for now, we don't need to take care of them
        return False

    def authorization_header(self, request=None) -> str:
        # request will be the Flask request object
        return None

    def current_user(self, request=None) -> User:
        # request will be the Flask request object
        return None
