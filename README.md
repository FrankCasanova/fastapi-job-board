# fastapi-job-board

![](backend/static/images/lite.gif)

I build a job board website, In which we will be having:

    List a job
    Details of the Job post
    Create a job post
    Update the job
    Delete the job
    Permissions (Authorization required, only superuser and the original author can delete)
    Authentication ( Registration and Login )
    Test our Endpoints
    Test Coverage
    Webapp for Jobboard

I follow something called Test-Driven Development in which we will be creating a unit-test for each of the components.



## Technology Stack:
* FastAPI
* Uvicorn (server)
* Pytest
* Sqlalchemy
* Postgres


## How to start the app ?
```
git clone https://github.com/frankcasanova/fastapi-job-board.git
cd fastapi-job-board/
pipenv shell
cd backend/
uvicorn main:app --reload     #start server
visit  127.0.0.1:8000/
```

Features:
 - ✔️ Serving Template
 - ✔️ Static Files in Development
 - ✔️ Connecting to Database
 - ✔️ Schemas
 - ✔️ Dependency Injection
 - ✔️ Password Hashing
 - ✔️ Unit Testing (What makes an app stable)
 - ✔️ Authentication login/create user/get token
 - ✔️ Authorization/Permissions 
 - ✔️ Webapp (Monolithic)
 - 🚧 Load Testing using Locust
 - 🚧 Fully Asyc
 - 🚧 Migration by alembic
 - 🚧 Caching
 - 🚧 Dockerization
 - 🚧 Creating a frontend using Vue/React
 - 🚧 Getting ready for Production e.g. load balancing,NGINX,HTTPS 
 - 🚧 Deployment
 - 🚧 CI and CD
