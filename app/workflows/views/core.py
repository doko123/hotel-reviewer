import logging

from flask import jsonify, Response, render_template, redirect, url_for, request
from flask_restful import Resource

from workflows.use_cases import review_hotel

logger = logging.getLogger(__name__)


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
            (
                score,
                comments_qty,
                hotel_providers,
                hotel_title,
                loc_title,
            ) = review_hotel.HotelReviewUseCase().review_hotel(
                hotel_name, location
            )
            print(f"Sending response with {hotel_name} and {location}")
            return Response(
                render_template(
                    "home.html",
                    hotel_title=hotel_title if hotel_title else hotel_name,
                    hotel_location=loc_title if loc_title else location,
                    score=score,
                    comments_qty=comments_qty,
                    hotel_providers=hotel_providers,
                    errors=False if score else True,
                ),
                mimetype="text/html",
            )

            return Response(
                render_template(
                    "home.html",
                    hotel_title="Sheraton Warsaw Hotel",
                    hotel_location="Warsaw",
                    score=11,
                    comments_qty=123,
                    hotel_providers="booking.com",
                    errors=False if 0 else True,
                ),
                mimetype="text/html",
            )
        return redirect(url_for("homepageresource"))
