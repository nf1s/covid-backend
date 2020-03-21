from sanic import Blueprint

from .cases import cases

api = Blueprint.group(cases, url_prefix="/api")
