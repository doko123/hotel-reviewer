import os

ELASTICSEARCH_INDEX = "hotel_index"
TEXT_ANALYTICS_BASE_URL = (
    "https://westcentralus.api.cognitive.microsoft.com/text/analytics/v2.0/"
)
SUBSCRIPTION_API_KEY = os.environ.get("SUBSCRIPTION_API_KEY")
AZURE_OUTDATED = os.environ.get("AZURE_OUTDATED")
DEBUG = os.environ.get("DEBUG", False)
TESTING = os.environ.get("TESTING", False)
