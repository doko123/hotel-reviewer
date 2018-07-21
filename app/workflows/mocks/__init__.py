from workflows.mocks.positive_comments import (
    comments_per_hotel as good_opinions
)
from workflows.mocks.negative_comments import comments_per_hotel as bad_opinions
import uuid


def get_positive(hotel_name):
    opinions = good_opinions.get(hotel_name, [])
    return [{"id": str(uuid.uuid4()), "text": text} for text in opinions]


def get_negative(hotel_name):
    opinions = bad_opinions.get(hotel_name, [])
    return [{"id": str(uuid.uuid4()), "text": text} for text in opinions]


def get_all(hotel_name):
    return get_positive(hotel_name) + get_positive(hotel_name)
