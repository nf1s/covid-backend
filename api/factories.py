from faker import Faker
from dataclasses import asdict, dataclass

fake = Faker(locale="en")


@dataclass
class CovidModelFactory:
    id: int = fake.pyint(min_value=0, max_value=9999, step=1)
    country: str = fake.country()
    confirmed: int = fake.pyint(min_value=0, max_value=9999, step=1)
    active: int = fake.pyint(min_value=0, max_value=9999, step=1)
    deaths: int = fake.pyint(min_value=0, max_value=9999, step=1)
    recovered: int = fake.pyint(min_value=0, max_value=9999, step=1)
    latitude: int = fake.latitude()
    longitude: int = fake.longitude()
    last_update: int = fake.pyint(min_value=0, max_value=999999, step=1)

    def to_dict(self):
        return asdict(self)


class CovidListFactory:
    data = [CovidModelFactory().to_dict() for num in range(1, 10)]


@dataclass
class StatsModelFactory:
    value: int = fake.pyint(min_value=0, max_value=9999, step=1)

    def to_dict(self):
        return asdict(self)


@dataclass
class CountryModelFactory:
    id: int = fake.pyint(min_value=0, max_value=9999, step=1)
    name: str = fake.country()

    def to_dict(self):
        return asdict(self)


class CountryListFactory:
    data = [CountryModelFactory().to_dict() for num in range(1, 10)]
