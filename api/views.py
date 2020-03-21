
from sanic import Blueprint
from covid import Covid
from sanic.response import json
from schematics.models import Model
from schematics.types import IntType
from schematics.types import StringType
from sanic_transmute import describe


class CovidModel(Model):
    id = IntType()
    country = StringType()
    confirmed = IntType()
    active = IntType()
    deaths = IntType()
    recovered = IntType()
    latitude = IntType()
    longitude = IntType()
    last_update = IntType()
    
    

@describe(paths="/data", methods="GET")
async def get_all(request):
    _covid = Covid()
    data = _covid.get_data()
    return {"data": data}


@describe(paths="/country/name={name}/", methods="GET")
async def get_status_by_name(request, name: str):
    _covid = Covid()
    data = _covid.get_status_by_country_name(name)
    return {"data": data}


@describe(paths="/country/id={id}/", methods="GET")
async def get_status_by_id(request, id):
    _covid = Covid()
    data = _covid.get_status_by_country_id(id)
    return {"data": data}


@describe(paths="/active", methods="GET")
async def get_active_cases(request):
    _covid = Covid()
    data = _covid.get_total_active_cases()
    return {"data": data}


@describe(paths="/confirmed", methods="GET")
async def get_confirmed_cases(request):
    _covid = Covid()
    data = _covid.get_total_confirmed_cases()
    return {"data": data}


@describe(paths="/recovered", methods="GET")
async def get_recovered_cases(request):
    _covid = Covid()
    data = _covid.get_total_recovered()
    return {"data": data}


@describe(paths="/deaths", methods="GET")
async def get_deaths(request):
    _covid = Covid()
    data = _covid.get_total_deaths()
    return {"data": data}
