import pytest

from workflows.providers.comments import booking


@pytest.mark.skip(reason="no way of currently testing this becuse of timeout")
def test_booking(hotel_reviews):
    # GIVEN
    hotel_name = "Sheraton"
    location = "Warszawa"
    # expected_comments = [review["text"] for review in hotel_reviews]

    # WHEN
    scrapper = booking.BookingScrapper(hotel_name, location)
    scrapper.scrape()

    # THEN

    assert scrapper.reviews
    returned_comments = [review["text"] for review in scrapper.reviews]
    assert returned_comments
