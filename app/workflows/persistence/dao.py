from config import settings


class TweetDao:
    def __init__(self, db):
        self.db = db

    def add_db_object(self, tweet):
        self.db.index(
            index=settings.ELASTICSEARCH_INDEX,
            doc_type="tweet",
            id=1,
            body=tweet,
        )
        tweet["timestamp"] = tweet["timestamp"].strftime("%Y-%m-%dT%H:%M:%S.%f")
        return tweet
