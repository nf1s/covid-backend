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


@dataclass
class CovidListFactory:
    data = [CovidModelFactory().to_dict() for num in range(1, 10)]


@dataclass
class StatsModelFactory:
    value = fake.pyint(min_value=0, max_value=9999, step=1)

    def to_dict(self):
        return asdict(self)


@dataclass
class CountryModelFactory:
    id = fake.pyint(min_value=0, max_value=9999, step=1)
    name = fake.country()

    def to_dict(self):
        return asdict(self)
