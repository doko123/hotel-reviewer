from workflows.providers.microsoft import MicrosoftManager


def test_get_languages(language_comments, expected_language_response):
    # GIVEN & WHEN
    documents_with_language = MicrosoftManager().detect_languages(
        language_comments
    )

    # THEN
    assert documents_with_language == expected_language_response


def test_get_sentiment_measured(sentiment_request_body):
    # GIVEN
    expected_score = 51.320

    # WHEN
    sentiment_score = MicrosoftManager().get_sentiment_measured(
        sentiment_request_body
    )

    # THEN
    assert sentiment_score == expected_score


def test_failed_request(malformed_data):
    # GIVEN
    expected_response = {"documents": []}

    # WHEN
    sentiment_score = MicrosoftManager().get_sentiment_measured(malformed_data)

    # THEN
    assert sentiment_score == expected_response
