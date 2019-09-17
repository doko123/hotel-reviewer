from datetime import datetime
import pytest

from dynaconf import settings
from flask.helpers import url_for


@pytest.fixture
def db(es):
    try:
        es.indices.delete(index=settings.ELASTICSEARCH_INDEX)
    except:
        pass
    doc = {
        "author": "Dominika Kowalczyk",
        "text": "Per aspera ad astra",
        "timestamp": datetime.now(),
        "hotel": "Lala Land",
        "location": "Las",
    }

    es.index(
        index=settings.ELASTICSEARCH_INDEX, doc_type="tweet", id=1, body=doc
    )
    doc["timestamp"] = doc["timestamp"].strftime("%Y-%m-%dT%H:%M:%S.%f")

    return es


def test_healthcheck(client):
    # GIVEN
    healthcheck_url = url_for("healthcheckresource")
    expected_response = {"status": "OK"}

    # WHEN
    response = client.get(healthcheck_url)

    # THEN
    assert response.status_code == 200
    assert expected_response == response.json


def test_es_index_get_by_id_should_return_one(db):

    # GIVEN & WHEN & THEN
    expected_total_found = 1
    expected_doc_id = "1"

    res = db.get(index=settings.ELASTICSEARCH_INDEX, doc_type="tweet", id=1)

    assert expected_doc_id == res["_id"]

    db.indices.refresh(index=settings.ELASTICSEARCH_INDEX)

    res = db.search(
        index=settings.ELASTICSEARCH_INDEX, body={"query": {"match_all": {}}}
    )

    assert expected_total_found == res["hits"]["total"]


def test_es_index_get_by_hotel_and_location_should_return_one(db):

    # GIVEN & WHEN & THEN
    expected_total_found = 1
    expected_doc_id = "2"
    doc_2 = {
        "author": "Dominika Kowalczyk",
        "text": "Per aspera ad astra",
        "timestamp": datetime.now(),
        "hotel": "hilton",
        "location": "lodz",
    }

    db.index(
        index=settings.ELASTICSEARCH_INDEX, doc_type="tweet", id=2, body=doc_2
    )
    doc_2["timestamp"] = doc_2["timestamp"].strftime("%Y-%m-%dT%H:%M:%S.%f")

    db.indices.refresh(index=settings.ELASTICSEARCH_INDEX)

    res = db.search(
        index=settings.ELASTICSEARCH_INDEX,
        body={"query": {"bool": {"must": {"match": {"hotel": "hilton"}}}}},
    )

    assert expected_total_found == res["hits"]["total"]
    assert doc_2 == res["hits"]["hits"][0]["_source"]
    assert expected_doc_id == res["hits"]["hits"][0]["_id"]


def test_es_index_get_by_hotel_and_location_should_return_1one(db):

    # GIVEN & WHEN & THEN
    expected_total_found = 1
    expected_doc_id = "2"
    doc_2 = {
        "author": "Dominika Kowalczyk",
        "text": "Per aspera ad astra",
        "timestamp": datetime.now(),
        "hotel": "hilton",
        "location": "lodz",
    }

    db.index(
        index=settings.ELASTICSEARCH_INDEX, doc_type="tweet", id=2, body=doc_2
    )
    doc_2["timestamp"] = doc_2["timestamp"].strftime("%Y-%m-%dT%H:%M:%S.%f")

    db.indices.refresh(index=settings.ELASTICSEARCH_INDEX)

    res = db.search(
        index=settings.ELASTICSEARCH_INDEX,
        body={
            "query": {
                "bool": {
                    "must": [
                        {"match": {"hotel": "hilton"}},
                        {"match": {"location": "lodz"}},
                    ]
                }
            }
        },
    )

    assert expected_total_found == res["hits"]["total"]
    assert doc_2 == res["hits"]["hits"][0]["_source"]
    assert expected_doc_id == res["hits"]["hits"][0]["_id"]
