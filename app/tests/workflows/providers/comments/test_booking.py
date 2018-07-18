from workflows.providers.comments import booking


def test_booking():
    booking.hotel_scrapper("Sheraton", "Sopot")
