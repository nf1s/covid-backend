from sanic import Blueprint
from sanic_transmute import add_route
from .views import (
    get_all,
    get_status_by_id,
    get_status_by_name,
    get_deaths,
    get_active_cases,
    get_recovered_cases,
    get_confirmed_cases,
)

cases = Blueprint("cases", url_prefix="/cases")
add_route(cases, get_all)
add_route(cases, get_status_by_id)
add_route(cases, get_status_by_name)
add_route(cases, get_deaths)
add_route(cases, get_active_cases)
add_route(cases, get_recovered_cases)
add_route(cases, get_confirmed_cases)
