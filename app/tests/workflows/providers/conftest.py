import pytest


@pytest.fixture
def language_comments():
    return [
        {"id": "1", "text": "This is a document written in English."},
        {"id": "2", "text": "Este es un document escrito en Español."},
        {"id": "3", "text": "这是一个用中文写的文件"},
    ]


@pytest.fixture
def sentiment_request_body():
    return [
        {
            "id": "1",
            "language": "en",
            "text": "I had a wonderful experience! "
            "The rooms were wonderful and the staff was helpful.",
        },
        {
            "id": "2",
            "language": "en",
            "text": "I had a terrible time at the hotel. "
            "The staff was rude and the food was awful.",
        },
        {
            "id": "3",
            "language": "es",
            "text": "Los caminos que llevan hasta Monte Rainier"
            "son espectaculares y hermosos.",
        },
        {
            "id": "4",
            "language": "es",
            "text": "La carretera estaba atascada. "
            "Había mucho tráfico el día de ayer.",
        },
    ]


@pytest.fixture
def expected_language_response():
    return {
        "documents": [
            {
                "id": "1",
                "text": "This is a document written in English.",
                "language": ["en"],
            },
            {
                "id": "2",
                "text": "Este es un document escrito en Español.",
                "language": ["es"],
            },
            {"id": "3", "text": "这是一个用中文写的文件", "language": ["zh_chs"]},
        ]
    }


@pytest.fixture
def expected_sentiment_response():
    return {
        "documents": [
            {"score": 0.92, "id": "1"},
            {"score": 0.85, "id": "2"},
            {"score": 0.34, "id": "3"},
        ],
        "errors": None,
    }


@pytest.fixture
def malformed_data():
    return [
        {"id": "1", "TEST": "This is a document written in English."},
        {"IDid": "2", "text": "Este es un document escrito en Español."},
    ]


@pytest.fixture
def hotel_reviews():
    import json

    with open("workflows/mocks/hotel_reviews.py") as f:
        return json.load(f)
