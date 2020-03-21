
from sanic import Blueprint
from covid import Covid
from sanic.response import json

cases = Blueprint('cases', url_prefix='/cases')


@cases.route("/data")
async def get_all(request):
    _covid = Covid()
    data = _covid.get_data()
    return json({"data": data})


@cases.route("/country/name=<name>")
async def get_status_by_name(request, name):
    _covid = Covid()
    data = _covid.get_status_by_country_name(name)
    return json({"data": data})


@cases.route("/country/id=<id>")
async def get_status_by_id(request, id):
    _covid = Covid()
    data = _covid.get_status_by_country_id(id)
    return json({"data": data})


@cases.route("/active")
async def get_active_cases(request):
    _covid = Covid()
    data = _covid.get_total_active_cases()
    return json({"data": data})


@cases.route("/confirmed")
async def get_confirmed_cases(request):
    _covid = Covid()
    data = _covid.get_total_confirmed_cases()
    return json({"data": data})


@cases.route("/recovered")
async def get_recovered_cases(request):
    _covid = Covid()
    data = _covid.get_total_recovered()
    return json({"data": data})


@cases.route("/deaths")
async def get_deaths(request):
    _covid = Covid()
    data = _covid.get_total_deaths()
    return json({"data": data})
