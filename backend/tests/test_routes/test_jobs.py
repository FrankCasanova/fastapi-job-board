import json

from starlette import status

# from pdb import set_trace


def test_create_job(
    client, normal_user_token_headers
):  # added normal_user_token_headers
    data = {
        "title": "SDE super",
        "company": "doogle",
        "company_url": "www.doogle.com",
        "location": "USA,NY",
        "description": "python",
        "date_posted": "2022-03-20",
    }
    response = client.post(
        "/jobs/create-job/", data=json.dumps(data), headers=normal_user_token_headers
    )  # added header in the post request
    assert response.status_code == 200
    assert response.json()["company"] == "doogle"
    assert response.json()["description"] == "python"


def test_read_job(client, normal_user_token_headers):
    """
    GIVEN a FastAPI application
    WHEN the '/jobs' page is requested (GET)
    THEN check the response is valid
    """
    data1 = dict(
        title="sde-super",
        company="doogle",
        company_url="https://www.doogle.com",
        location="somewhere",
        description="python",
        date_posted="2020-01-01",
    )

    response = client.post(
        "/jobs/create-job/", data=json.dumps(data1), headers=normal_user_token_headers
    )

    response = client.get("/jobs/get/2/")
    assert response.status_code == 200
    assert response.json()["title"] == "sde-super"
    assert response.json()["company"] == "doogle"


def test_read_all_jobs(client, normal_user_token_headers):
    data = dict(
        title="sde super",
        company="doogle",
        company_url="https://www.doogle.com",
        location="somewhere",
        description="python",
        date_posted="2020-01-01",
    )

    client.post(
        "/jobs/create-job/", json.dumps(data), headers=normal_user_token_headers
    )
    client.post(
        "/jobs/create-job/", json.dumps(data), headers=normal_user_token_headers
    )

    response = client.get("/jobs/all/")

    assert response.status_code == 200
    assert response.json()[0]
    assert response.json()[1]


def test_update_a_job(client):
    data = {
        "title": "test-update-job",
        "company": "doogle",
        "company_url": "www.doogle.com",
        "location": "USA,NY",
        "description": "fastapi",
        "date_posted": "2022-03-20",
    }
    client.post("/jobs/create-job/", json.dumps(data))
    data["title"] = "test new title"
    response = client.put("/jobs/update/1", json.dumps(data))
    assert response.json()["msg"] == "Successfully updated data."


def test_delete_a_job(client, normal_user_token_headers):  # new
    data = {
        "title": "test-delete-job",
        "company": "doogle",
        "company_url": "www.doogle.com",
        "location": "USA,NY",
        "description": "fastapi",
        "date_posted": "2022-03-20",
    }
    client.post(
        "/jobs/create-job/", json.dumps(data), headers=normal_user_token_headers
    )

    client.delete("/jobs/delete/5", headers=normal_user_token_headers)
    response = client.get("/jobs/get/5/")
    assert response.status_code == status.HTTP_404_NOT_FOUND
