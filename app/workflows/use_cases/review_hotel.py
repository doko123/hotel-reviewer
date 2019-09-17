import logging

from workflows.dry_provider.mixed_comments import processed_tweets
from workflows.providers.comments import booking
from workflows.providers.microsoft import MicrosoftManager

logger = logging.getLogger(__name__)


class HotelReviewUseCase:
    def review_hotel(self, hotel_name, location):
        recognized_comments = []
        # fetch_comments: list of contents
        print("Fetching comments")
        scrapper = booking.BookingScrapper(hotel_name, location)
        scrapper.scrape()
        reviews = processed_tweets()
        print(f"Fetched {len(scrapper.reviews) or len(reviews)} comments")
        tweets = scrapper.reviews or reviews
        if not tweets:
            scrapper.selenium_setup.tear_down()
            return (
                0,
                len(scrapper.reviews),
                "booking.com",
                scrapper.hotel_title,
                scrapper.hotel_location_title,
            )

        if scrapper.reviews:
            # detect language for comments
            recognized_comments = MicrosoftManager().detect_languages(
                scrapper.reviews
            )
        else:
            recognized_comments = tweets
            print(len(recognized_comments))
        return (
            MicrosoftManager().get_sentiment_measured(recognized_comments),
            len(recognized_comments),
            "booking.com",
            scrapper.hotel_title,
            scrapper.hotel_location_title,
        )
