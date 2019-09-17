from datetime import datetime

import attr


@attr.s
class Tweet:
    autor = attr.ib()
    text = attr.ib()
    score = attr.ib()
    hotel_name = attr.ib()
    hotel_location = attr.ib()
    date_published = attr.ib()
    timestamp = attr.ib(default=datetime.utcnow().replace(microsecond=0))
