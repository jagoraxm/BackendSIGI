from tests.commons import *


def test_app_test_get_200(headers, test_client):
    """
    GIVEN the headers from the request and
    WHEN authentication is verified
    THEN check the data of user, and return the Tickets array
    """
    response = test_client.get("/service/api/appTest/v1", headers=headers)

    assert response.status_code == 200


def test_app_test_post_201(headers, request_body_test, test_client):
    """
    GIVEN the headers and body request from the request and
    WHEN authentication is verified
    THEN to create new resource with the data of body request
    """
    response = test_client.post(
        "/service/api/appTest/v1", headers=headers, json=request_body_test
    )

    assert response.status_code == 201
