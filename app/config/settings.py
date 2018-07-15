import os

ELASTICSEARCH_INDEX = "hotel_index"
TEXT_ANALYTICS_BASE_URL = (
    "https://westcentralus.api.cognitive.microsoft.com/text/analytics/v2.0/"
)
SUBSCRIPTION_API_KEY = os.environ.get("SUBSCRIPTION_API_KEY")
