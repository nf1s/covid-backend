from sanic import Blueprint

from .urls import cases

api = Blueprint.group(cases, url_prefix="/v1")


__all__ = ["api"]
