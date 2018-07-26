from workflows.mocks import get_all
from workflows.providers.microsoft import MicrosoftManager


class HotelReviewUseCase:
    def review_hotel(self, hotel_name):

        # fetch_comments: list of contents
        comments = get_all(hotel_name)

        # detect language for comments
        recognized_comments = MicrosoftManager().detect_languages(comments)
        return MicrosoftManager().get_sentiment_measured(recognized_comments)
