from flask import jsonify, Flask, Response, render_template, redirect, url_for, request
from flask_restful import Resource

from workflows.use_cases import review_hotel



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
        hotel_name = request.form["hotel_name"]
        if not hotel_name:
            return redirect(url_for("homepageresource"))

        return review_hotel.HotelReviewUseCase().review_hotel(hotel_name)
