from flask import jsonify
from flask_restful import Resource


class HealthCheckResource(Resource):
    def get(self):
        return jsonify({"status": "OK"})
