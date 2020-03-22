
from sanic_transmute import describe
from .models import CovidModel, CountryModel, StatsModel
from api import controller


@describe(paths="/all", methods="GET")
async def get_all(request) -> [CovidModel]:
    data = await controller.get_all()
    return data


@describe(paths="/list-countries", methods="GET")
async def list_countries(request) -> [CountryModel]:
    data = await controller.list_countries()
    return data


@describe(paths="/country/name={name}/", methods="GET")
async def get_status_by_country_name(request, name: str) -> CovidModel:
    data = await controller.get_status_by_country_name(name)
    return data


@describe(paths="/country/id={id}/", methods="GET")
async def get_status_by_country_id(request, id: int) -> CovidModel:
    data = await controller.get_status_by_country_id(id)
    return data


@describe(paths="/active", methods="GET")
async def get_active_cases(request) -> StatsModel:
    data = await controller.get_active_cases()
    return data


@describe(paths="/confirmed", methods="GET")
async def get_confirmed_cases(request) -> StatsModel:
    data = await controller.get_confirmed_cases()
    return data


@describe(paths="/recovered", methods="GET")
async def get_recovered_cases(request) -> StatsModel:
    data = await controller.get_recovered_cases()
    return data


@describe(paths="/deaths", methods="GET")
async def get_deaths(request) -> StatsModel:
    data = await controller.get_deaths()
    return data
