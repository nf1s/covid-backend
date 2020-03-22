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


async def test_get_country_name(test_client, app):
    url = app.url_for("cases.get_status_by_country_name", name="spain")
    resp = await test_client.get(url)
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


async def test_get_country_id(test_client, app):
    url = app.url_for("cases.get_status_by_country_id", id=50)
    resp = await test_client.get(url)
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


async def test_get_all_data(test_client, app):
    url = app.url_for("cases.get_all")
    resp = await test_client.get(url)
    assert resp.status == status.OK

    resp_json = await resp.json()
    assert type(resp_json) is list
    data = resp_json[0]
    assert type(data) is dict
    assert "country" in data
    assert "confirmed" in data
    assert "active" in data
    assert "deaths" in data
    assert "recovered" in data
    assert "latitude" in data
    assert "longitude" in data
    assert "last_update" in data


async def test_list_country(test_client, app):
    url = app.url_for("cases.list_countries")
    resp = await test_client.get(url)
    assert resp.status == status.OK

    resp_json = await resp.json()
    assert type(resp_json) is list
    data = resp_json[0]
    assert type(data) is dict
    assert "id" in data
    assert "name" in data


async def test_active_cases(test_client, app):
    url = app.url_for("cases.get_active_cases")
    resp = await test_client.get(url)
    assert resp.status == status.OK

    data = await resp.json()
    assert type(data) is dict
    assert type(data["value"]) is int


async def test_confirmed_cases(test_client, app):
    url = app.url_for("cases.get_confirmed_cases")
    resp = await test_client.get(url)
    assert resp.status == status.OK

    data = await resp.json()
    assert type(data) is dict
    assert type(data["value"]) is int


async def test_recovered_cases(test_client, app):
    url = app.url_for("cases.get_recovered_cases")
    resp = await test_client.get(url)
    assert resp.status == status.OK

    data = await resp.json()
    assert type(data) is dict
    assert type(data["value"]) is int


async def test_deaths(test_client, app):
    url = app.url_for("cases.get_deaths")
    resp = await test_client.get(url)
    assert resp.status == status.OK

    data = await resp.json()
    assert type(data) is dict
    assert type(data["value"]) is int
