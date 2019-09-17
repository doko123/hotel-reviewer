from flask.helpers import url_for
from mock import patch


def test_hotel_review(client, hotel_reviews):
    # GIVEN
    review_url = url_for("homepageresource")
    expected_result = (
        b"The positive reviews of Sheraton Warsaw Hotel in Warsaw is "
        b"calculated on 1 comments from booking.com"
    )

    # WHEN
    with patch(
        "workflows.providers.comments.booking.BookingScrapper"
    ) as mocked:
        instance = mocked.return_value

        instance.reviews = hotel_reviews
        instance.hotel_location_title = "Warsaw"
        instance.hotel_title = "Sheraton Warsaw Hotel"
        instance.scrape.return_value = None
        response = client.post(
            review_url,
            data=dict(hotel_name="Sheraton", location="Warszawa"),
            follow_redirects=True,
        )

    # THEN
    assert response.status_code == 200
    assert expected_result in response.data
