
from covid import Covid
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
    

class StatsModel(Model):
    value = IntType()


class CountryModel(Model):
    id = IntType()
    name = StringType()


@describe(paths="/data", methods="GET")
async def get_all(request) -> [CovidModel]:
    _covid = Covid()
    data = _covid.get_data()
    return data

@describe(paths="/list-countries", methods="GET")
async def list_countries(request) -> [CountryModel]:
    _covid = Covid()
    data = _covid.list_countries()
    return data


@describe(paths="/country/name={name}/", methods="GET")
async def get_status_by_name(request, name: str) -> CovidModel:
    _covid = Covid()
    data = _covid.get_status_by_country_name(name)
    return data


@describe(paths="/country/id={id}/", methods="GET")
async def get_status_by_id(request, id) -> CovidModel:
    _covid = Covid()
    data = _covid.get_status_by_country_id(id)
    return data


@describe(paths="/active", methods="GET")
async def get_active_cases(request) -> StatsModel:
    _covid = Covid()
    data = _covid.get_total_active_cases()
    return {"value": data}


@describe(paths="/confirmed", methods="GET")
async def get_confirmed_cases(request) -> StatsModel:
    _covid = Covid()
    data = _covid.get_total_confirmed_cases()
    return {"value": data}


@describe(paths="/recovered", methods="GET")
async def get_recovered_cases(request) -> StatsModel:
    _covid = Covid()
    data = _covid.get_total_recovered()
    return {"value": data}


@describe(paths="/deaths", methods="GET")
async def get_deaths(request) -> StatsModel:
    _covid = Covid()
    data = _covid.get_total_deaths()
    return {"value": data}
