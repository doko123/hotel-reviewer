from dynaconf import settings
import pytest

from workflows.providers.microsoft import MicrosoftManager


@pytest.mark.skipif(settings.AZURE_OUTDATED, reason="Response mocked")
def test_get_languages(language_comments, expected_language_response):
    # GIVEN & WHEN
    documents_with_language = MicrosoftManager().detect_languages(
        language_comments
    )

    # THEN
    assert documents_with_language == expected_language_response


@pytest.mark.skipif(settings.AZURE_OUTDATED, reason="Response mocked")
def test_get_sentiment_measured(sentiment_request_body):
    # GIVEN
    expected_score = 66.670

    # WHEN
    sentiment_score = MicrosoftManager().get_sentiment_measured(
        sentiment_request_body
    )

    # THEN
    assert sentiment_score == expected_score


@pytest.mark.skipif(settings.AZURE_OUTDATED, reason="Response mocked")
def test_failed_request(malformed_data):
    # GIVEN
    expected_response = {"documents": []}

    # WHEN
    sentiment_score = MicrosoftManager().get_sentiment_measured(malformed_data)

    # THEN
    assert sentiment_score == expected_response
