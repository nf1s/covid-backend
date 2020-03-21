from sanic import Sanic
from sanic.response import json

from covid import Covid

app = Sanic(__name__)


@app.route("/data")
async def get_all(request):
    _covid = Covid()
    stats = _covid.get_data()
    return json({"data": stats})


@app.route("/country/name=<name>")
async def get_status_by_name(request, name):
    _covid = Covid()
    data = _covid.get_status_by_country_name(name)
    return json({name.lower(): data})


@app.route("/country/id=<id>")
async def get_status_by_id(request, id):
    _covid = Covid()
    data = _covid.get_status_by_country_id(id)
    return json({data["country"].title(): data})


@app.route("/active")
async def get_active_cases(request):
    _covid = Covid()
    data = _covid.get_total_active_cases()
    return json({"cases": data})


@app.route("/confirmed")
async def get_confirmed_cases(request):
    _covid = Covid()
    data = _covid.get_total_confirmed_cases()
    return json({"cases": data})


@app.route("/recovered")
async def get_recovered_cases(request):
    _covid = Covid()
    data = _covid.get_total_recovered()
    return json({"cases": data})


@app.route("/deaths")
async def get_deaths(request):
    _covid = Covid()
    data = _covid.get_total_deaths()
    return json({"cases": data})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
