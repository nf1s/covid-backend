from sanic import Sanic
from sanic_transmute import add_swagger

from api import api


def create_app(**kwargs):
    app = Sanic(__name__)
    app.blueprint(api)
    add_swagger(app, "/api/swagger.json", "/api/docs")
    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, auto_reload=True)
