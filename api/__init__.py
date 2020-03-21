from sanic import Blueprint

from .urls import cases

api = Blueprint.group(cases, url_prefix="/api")


__all__ = ["api"]
