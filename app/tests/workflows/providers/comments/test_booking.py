from workflows.providers.comments import booking


def test_booking(hotel_reviews):
    # GIVEN
    hotel_name = "Sheraton"
    location = "Warszawa"
    expected_comments = [review["comment"] for review in hotel_reviews]

    # WHEN
    scrapper = booking.BookingScrapper(hotel_name, location)
    scrapper.scrape()

    # THEN
    returned_comments = [review["comment"] for review in scrapper.reviews]
    assert expected_comments == returned_comments
