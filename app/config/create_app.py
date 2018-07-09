import time

from elasticsearch import Elasticsearch
from flask import Flask
from flask_restful import Api
import redis

from workflows import views

cache = redis.Redis(host="redis", port=6379)


def setup_es():
    return Elasticsearch(hosts="elasticsearch:9200")


def create_app(testing=False):

    app = Flask(__name__)
    app.testing = testing
    app.url_map.strict_slashes = False
    app.config["PROPAGATE_EXCEPTIONS"] = True

    # setup elasticsearch
    es = setup_es()

    # creating api
    api = Api(app)

    # CORE ENDPOINTS
    # TODO: Make it available only for debug mode
    api.add_resource(views.HealthCheckResource, "/healthcheck/")

    return app, es


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr("hits")
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)
