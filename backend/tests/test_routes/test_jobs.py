import json

# from pdb import set_trace


def test_create_job(client):
    """
    GIVEN a FastAPI application
    WHEN the '/jobs' page is requested (GET)
    THEN check the response is valid
    """
    data = dict(
        title="sde super",
        company="doogle",
        company_url="https://www.doogle.com",
        location="somewhere",
        description="python",
        date_posted="2020-01-01",
    )
    response = client.post("/jobs/create-job/", json=data)
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.json()["company"] == "doogle"
    assert response.json()["title"] == "sde super"
    assert response.json()["company_url"] == "https://www.doogle.com"
    assert response.json()["location"] == "somewhere"
    assert response.json()["description"] == "python"
    assert response.json()["date_posted"] == "2020-01-01"


def test_read_job(client):
    """
    GIVEN a FastAPI application
    WHEN the '/jobs' page is requested (GET)
    THEN check the response is valid
    """
    data = dict(
        title="sde super",
        company="doogle",
        company_url="https://www.doogle.com",
        location="somewhere",
        description="python",
        date_posted="2020-01-01",
    )

    response = client.post("/jobs/create-job/", json.dumps(data))

    response = client.get("/jobs/get/1/")
    assert response.status_code == 200
    assert response.json() == {
        "title": "sde super",
        "company": "doogle",
        "company_url": "https://www.doogle.com",
        "location": "somewhere",
        "description": "python",
        "date_posted": "2020-01-01",
    }
