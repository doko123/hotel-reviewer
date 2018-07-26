from flask import (
    jsonify,
    Response,
    render_template,
    redirect,
    url_for,
    request,
)
from flask_restful import Resource

from workflows.use_cases import review_hotel


class HealthCheckResource(Resource):
    methods = ["GET"]

    def get(self):
        # TODO: Change to return number of cached hotels to encourage client to
        # fetch review
        return jsonify({"status": "OK"})


class HomePageResource(Resource):
    methods = ["GET", "POST"]

    def get(self):
        return Response(render_template("home.html"), mimetype="text/html")

    def post(self):
        hotel_name = request.form["hotel_name"]
        location = request.form["location"]
        if hotel_name and location:
            return review_hotel.HotelReviewUseCase().review_hotel(hotel_name)
        return redirect(url_for("homepageresource"))
