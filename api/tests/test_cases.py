from main import create_app
import pytest
from http import HTTPStatus as status


@pytest.yield_fixture
def app():
    app = create_app()
    yield app


@pytest.fixture
def test_client(loop, app, sanic_client):
    return loop.run_until_complete(sanic_client(app))


async def test_get_country_name(test_client):
    """
    GET request
    """
    resp = await test_client.get("/api/cases/country/name=spain")
    assert resp.status == status.OK

    data = await resp.json()
    assert type(data) is dict
    assert "country" in data
    assert "confirmed" in data
    assert "active" in data
    assert "deaths" in data
    assert "recovered" in data
    assert "latitude" in data
    assert "longitude" in data
    assert "last_update" in data
    assert data["country"] == "Spain"
