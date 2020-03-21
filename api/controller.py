from covid import Covid
from .models import CovidModel, StatsModel, CountryModel


async def get_all() -> [CovidModel]:
    _covid = Covid()
    data = _covid.get_data()
    return data


async def list_countries() -> [CountryModel]:
    _covid = Covid()
    data = _covid.list_countries()
    return data


async def get_status_by_country_name(name: str) -> CovidModel:
    _covid = Covid()
    data = _covid.get_status_by_country_name(name)
    return data


async def get_status_by_country_id(id: int) -> CovidModel:
    _covid = Covid()
    data = _covid.get_status_by_country_id(id)
    return data


async def get_active_cases() -> StatsModel:
    _covid = Covid()
    data = _covid.get_total_active_cases()
    return {"value": data}


async def get_confirmed_cases() -> StatsModel:
    _covid = Covid()
    data = _covid.get_total_confirmed_cases()
    return {"value": data}


async def get_recovered_cases() -> StatsModel:
    _covid = Covid()
    data = _covid.get_total_recovered()
    return {"value": data}


async def get_deaths() -> StatsModel:
    _covid = Covid()
    data = _covid.get_total_deaths()
    return {"value": data}
