from flask import jsonify, Flask, Response, render_template, redirect, url_for, request
from flask_restful import Resource



class HealthCheckResource(Resource):
    methods = ["GET"]

    def get(self):
        # TODO: Change to return number of cached hotels
        return jsonify({"status": "OK"})


class HomePageResource(Resource):
    methods = ["GET", "POST"]

    def get(self):

        return Response(render_template("home.html"), mimetype="text/html")

    def post(self):
        if not request.form["hotel_name"]:
            return redirect(url_for("homepageresource"))
        

