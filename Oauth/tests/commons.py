import pytest
import requests
from main import create_app

from config import Settings

config = Settings()


@pytest.fixture(scope="module")
def test_client():
    app = create_app()

    with app.test_client() as test_client:
        return test_client


@pytest.fixture
def mock_data():
    return {
        "name": "RICARDO CERVANTES LOPEZ",
        "email": "ricardo.cervantes@edu.utc.mx",
        "studentId": 346901,
        "studentEnrollmentNumber": "220055315",
        "curp": "HEAE911221HDFRND06",
        "academicLevel": "BACHILLERATO",
        "academicLevelCode": "BA",
        "program": "BACH TECNOLÓGICO EN TURISMO",
        "campus": "PLANTEL COACALCO",
        "phoneNumber": "5554279078",
        "modality": "A Distancia",
        "privacyNotice": {
            "privacy_notice_agreed": True,
            "terms_and_conditions_agreed": True,
            "promotions_and_discounts": False,
        },
        "webApp": {
            "url": "https://app-campusvirtual-dev.azurewebsites.net",
            "school": "UTC",
        },
        "permissions": {
            "SES": True,
            "ATT": True,
            "PRF": True,
            "CLS": True,
            "AYC": True,
            "PRO": True,
            "INT": True,
            "DOA": True,
            "COE": True,
            "BIB": True,
            "IDU": True,
            "BEC": True,
            "HIA": True,
            "CEE": True,
            "LOG": True,
            "CAE": True,
            "EQU": True,
            "ATA": True,
            "TUT": True,
            "REE": True,
            "CAP": True,
            "PAF": True,
            "CRE": True,
            "REI": True,
            "CLA": True,
            "TIT": True,
        },
    }


@pytest.fixture
def header_auth_ok():
    url = "https://app-cv-oauth-dev.azurewebsites.net/createTokens"
    response = requests.post(url).json()

    body = {"refreshToken": response["refreshToken"]}

    url2 = "https://app-cv-oauth-dev.azurewebsites.net/refreshToken"

    response2 = requests.post(url2, json=body).json()

    return response2["accessToken"]


@pytest.fixture
def header_auth_ok_with_data(mock_data):
    url = "https://app-cv-oauth-dev.azurewebsites.net/createTokens"
    response = requests.post(url, json=mock_data).json()

    body = {"refreshToken": response["refreshToken"]}

    url2 = "https://app-cv-oauth-dev.azurewebsites.net/refreshToken"

    response2 = requests.post(url2, json=body).json()

    return response2["accessToken"]


@pytest.fixture
def headers(header_auth_ok):
    headers = {
        "Authorization": header_auth_ok,
        "Service-id": config.service_id,
        "Service-name": config.service_name,
    }
    return headers


@pytest.fixture
def headers_data(header_auth_ok_with_data):
    headers = {
        "Authorization": header_auth_ok_with_data,
        "Service-id": "service-id-api",
        "Service-name": "service-name",
    }
    return headers


@pytest.fixture
def headers_null_auth():
    headers = {
        "Authorization": "",
        "Service-id": "service-id-api",
        "Service-name": "service-name",
    }
    return headers


@pytest.fixture
def headers_null_id(header_auth_ok):
    headers = {
        "Authorization": header_auth_ok,
        "Service-id": "",
        "Service-name": "service-name",
    }
    return headers


@pytest.fixture
def headers_null_name(header_auth_ok):
    headers = {
        "Authorization": header_auth_ok,
        "Service-id": "service-id-api",
        "Service-name": "",
    }
    return headers


@pytest.fixture
def header_auth_invalid():
    headers = {
        "Authorization": "holaeyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiUklDQVJETyBDRVJWQU5URVMgTE9QRVoiLCJlbWFpbCI6InJpY2FyZG8uY2VydmFudGVzQGVkdS51dGMubXgiLCJzdHVkZW50SWQiOjM0NjkwMSwic3R1ZGVudEVucm9sbG1lbnROdW1iZXIiOiJVOTkzNDQyNTQiLCJjdXJwIjoiSEVBRTkxMTIyMUhERlJORDA2IiwiYWNhZGVtaWNMZXZlbCI6IkJBQ0hJTExFUkFUTyIsImFjYWRlbWljTGV2ZWxDb2RlIjoiQkEiLCJwcm9ncmFtIjoiQkFDSCBURUNOT0zDk0dJQ08gRU4gVFVSSVNNTyIsImNhbXB1cyI6IlBMQU5URUwgQ09BQ0FMQ08iLCJwaG9uZU51bWJlciI6IjU1NTQyNzkwNzgiLCJtb2RhbGl0eSI6IkEgRGlzdGFuY2lhIiwicHJpdmFjeU5vdGljZSI6eyJwcml2YWN5X25vdGljZV9hZ3JlZWQiOnRydWUsInRlcm1zX2FuZF9jb25kaXRpb25zX2FncmVlZCI6dHJ1ZSwicHJvbW90aW9uc19hbmRfZGlzY291bnRzIjpmYWxzZX0sIndlYkFwcCI6eyJ1cmwiOiJodHRwczovL2FwcC1jYW1wdXN2aXJ0dWFsLWRldi5henVyZXdlYnNpdGVzLm5ldCIsInNjaG9vbCI6IlVUQyJ9LCJwZXJtaXNzaW9ucyI6eyJTRVMiOnRydWUsIkFUVCI6dHJ1ZSwiUFJGIjp0cnVlLCJDTFMiOnRydWUsIkFZQyI6dHJ1ZSwiUFJPIjp0cnVlLCJJTlQiOnRydWUsIkRPQSI6dHJ1ZSwiQ09FIjp0cnVlLCJCSUIiOnRydWUsIklEVSI6dHJ1ZSwiQkVDIjp0cnVlLCJISUEiOnRydWUsIkNFRSI6dHJ1ZSwiTE9HIjp0cnVlLCJDQUUiOnRydWUsIkVRVSI6dHJ1ZSwiQVRBIjp0cnVlLCJUVVQiOnRydWUsIlJFRSI6dHJ1ZSwiQ0FQIjp0cnVlLCJQQUYiOnRydWUsIkNSRSI6dHJ1ZSwiQ0xBIjp0cnVlLCJUSVQiOnRydWV9LCJpYXQiOjE2NDE1MDU5NzgsImV4cCI6MTY0MTUwNjg3OH0.hLLL0Xy-U9zn1gr3Plg2WfixLkTuJl-mKzcCE6ZkcJU",
        "Service-id": "service-id-api",
        "Service-name": "service-name",
    }
    return headers


@pytest.fixture
def header_auth_expired():
    headers = {
        "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiUklDQVJETyBDRVJWQU5URVMgTE9QRVoiLCJlbWFpbCI6InJpY2FyZG8uY2VydmFudGVzQGVkdS51dGMubXgiLCJzdHVkZW50SWQiOjM0NjkwMSwic3R1ZGVudEVucm9sbG1lbnROdW1iZXIiOiJVOTkzNDQyNTQiLCJjdXJwIjoiSEVBRTkxMTIyMUhERlJORDA2IiwiYWNhZGVtaWNMZXZlbCI6IkJBQ0hJTExFUkFUTyIsImFjYWRlbWljTGV2ZWxDb2RlIjoiQkEiLCJwcm9ncmFtIjoiQkFDSCBURUNOT0zDk0dJQ08gRU4gVFVSSVNNTyIsImNhbXB1cyI6IlBMQU5URUwgQ09BQ0FMQ08iLCJwaG9uZU51bWJlciI6IjU1NTQyNzkwNzgiLCJtb2RhbGl0eSI6IkEgRGlzdGFuY2lhIiwicHJpdmFjeU5vdGljZSI6eyJwcml2YWN5X25vdGljZV9hZ3JlZWQiOnRydWUsInRlcm1zX2FuZF9jb25kaXRpb25zX2FncmVlZCI6dHJ1ZSwicHJvbW90aW9uc19hbmRfZGlzY291bnRzIjpmYWxzZX0sIndlYkFwcCI6eyJ1cmwiOiJodHRwczovL2FwcC1jYW1wdXN2aXJ0dWFsLWRldi5henVyZXdlYnNpdGVzLm5ldCIsInNjaG9vbCI6IlVUQyJ9LCJwZXJtaXNzaW9ucyI6eyJTRVMiOnRydWUsIkFUVCI6dHJ1ZSwiUFJGIjp0cnVlLCJDTFMiOnRydWUsIkFZQyI6dHJ1ZSwiUFJPIjp0cnVlLCJJTlQiOnRydWUsIkRPQSI6dHJ1ZSwiQ09FIjp0cnVlLCJCSUIiOnRydWUsIklEVSI6dHJ1ZSwiQkVDIjp0cnVlLCJISUEiOnRydWUsIkNFRSI6dHJ1ZSwiTE9HIjp0cnVlLCJDQUUiOnRydWUsIkVRVSI6dHJ1ZSwiQVRBIjp0cnVlLCJUVVQiOnRydWUsIlJFRSI6dHJ1ZSwiQ0FQIjp0cnVlLCJQQUYiOnRydWUsIkNSRSI6dHJ1ZSwiQ0xBIjp0cnVlLCJUSVQiOnRydWV9LCJpYXQiOjE2NDE1MDc1MjYsImV4cCI6MTY0MTUwODQyNn0.Lxf-6__O_KdviufijPInNWQz4OqlXlqe-CKrQeV9x1I",
        "Service-id": "service-id-api",
        "Service-name": "service-name",
    }
    return headers


@pytest.fixture
def headers_not_auth():
    headers = {"Service-id": "service-id-api", "Service-name": "service-name"}
    return headers


@pytest.fixture
def headers_not_id(header_auth_ok):
    headers = {"Authorization": header_auth_ok, "Service-name": "service-name"}
    return headers


@pytest.fixture
def headers_not_name(header_auth_ok):
    headers = {
        "Authorization": header_auth_ok,
        "Service-id": "service-id-api",
    }
    return headers


@pytest.fixture
def mock_body_re():
    return {
        "chargeAccepted": True,
        "comments": "string",
        "files": [{"fileBody": "string", "fileName": "string", "fileType": "string"}],
        "phoneNumber": "string",
    }


@pytest.fixture
def request_body_test():
    return {
        "files": [{"fileBody": "string", "fileName": "string", "fileType": "string"}],
        "name": "edu",
    }
