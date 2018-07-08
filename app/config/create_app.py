import time

import redis
from flask import Flask

cache = redis.Redis(host="redis", port=6379)


def create_app(testing=False):

    app = Flask(__name__)
    app.testing = testing
    app.url_map.strict_slashes = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    return app


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
