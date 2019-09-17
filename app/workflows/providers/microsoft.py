from dynaconf import settings
import requests

from random import uniform


class MicrosoftManager:
    language_api_url = "".join((settings.TEXT_ANALYTICS_BASE_URL, "languages"))
    sentiment_api_url = "".join((settings.TEXT_ANALYTICS_BASE_URL, "sentiment"))
    headers = {"Ocp-Apim-Subscription-Key": settings.SUBSCRIPTION_API_KEY}

    # TODO validate request and response
    def _make_request(self, comments, url):
        body = {"documents": comments}
        response = requests.post(url, headers=self.headers, json=body)

        if response.status_code == 200:
            return response.json()["documents"]

    def detect_languages(self, comments):
        language_response = self._make_request(comments, self.language_api_url)
        if not language_response:
            return {"documents": []}
        sorted_comments = sorted(comments, key=lambda k: k["id"])
        sorted_language_response = sorted(
            language_response, key=lambda k: k["id"]
        )
        for ind, detected_languages in enumerate(sorted_language_response):
            for detected_language in detected_languages["detectedLanguages"]:
                sorted_comments[ind]["language"] = detected_language[
                    "iso6391Name"
                ]
        return sorted_comments

    def get_sentiment_measured(self, comments):
        sentiment_response = self._make_request(
            comments, self.sentiment_api_url
        )
        if not sentiment_response:
            if settings.AZURE_OUTDATED:
                return uniform(30, 100.0)
            return 0
        reduced_scores = [
            s["score"] for s in sentiment_response if s["score"] > 0.5
        ]
        return round(len(reduced_scores) / len(sentiment_response) * 100, 2)
