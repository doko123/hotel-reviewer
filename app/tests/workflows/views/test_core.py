from datetime import datetime

from dynaconf import settings
from flask.helpers import url_for


def test_healthcheck(client):
    # GIVEN
    healthcheck_url = url_for("healthcheckresource")
    expected_response = {"status": "OK"}

    # WHEN
    response = client.get(healthcheck_url)

    # THEN
    assert response.status_code == 200
    assert expected_response == response.json


def test_es(es):

    # GIVEN & WHEN & THEN
    expected_total_found = 1
    doc = {
        "author": "Dominika Kowalczyk",
        "text": "Per aspera ad astra",
        "timestamp": datetime.now(),
    }

    es.index(
        index=settings.ELASTICSEARCH_INDEX, doc_type="tweet", id=1, body=doc
    )
    doc["timestamp"] = doc["timestamp"].strftime("%Y-%m-%dT%H:%M:%S.%f")

    res = es.get(index=settings.ELASTICSEARCH_INDEX, doc_type="tweet", id=1)
    assert doc == res["_source"]

    es.indices.refresh(index=settings.ELASTICSEARCH_INDEX)

    res = es.search(
        index=settings.ELASTICSEARCH_INDEX, body={"query": {"match_all": {}}}
    )

    assert expected_total_found == res["hits"]["total"]
