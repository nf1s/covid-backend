from schematics.models import Model
from schematics.types import IntType
from schematics.types import StringType


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
