from workflows.providers.comments import booking
from workflows.providers.microsoft import MicrosoftManager


class HotelReviewUseCase:
    def review_hotel(self, hotel_name, location):

        # fetch_comments: list of contents
        scrapper = booking.BookingScrapper(hotel_name, location)
        scrapper.scrape()

        if not scrapper.reviews:
            scrapper.selenium_setup.tear_down()
            return (
                0,
                len(scrapper.reviews),
                "booking.com",
                scrapper.hotel_title,
                scrapper.hotel_location_title,
            )

        # detect language for comments
        recognized_comments = MicrosoftManager().detect_languages(
            scrapper.reviews
        )
        return (
            MicrosoftManager().get_sentiment_measured(recognized_comments),
            len(scrapper.reviews),
            "booking.com",
            scrapper.hotel_title,
            scrapper.hotel_location_title,
        )
