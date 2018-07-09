from flask_restful import Api

from config import create_app
from workflows import views


if __name__ == "__main__":

    app = create_app.create_app()
    api = Api(app)

    # CORE ENDPOINTS
    # TODO: Make it available only for debug mode
    api.add_resource(views.HealthCheckResource, "/healthcheck/")

    app.run(host="0.0.0.0", debug=True)
