# Abantether Home Task

This project written in Python 3.12 and use Django 5.0.2 with MySql database. Also used celery and redis for broker.

## Run project

All services running in docker. Then Docker and docker-compose are needed for running this project
```commandline
docker-compose up --build -d
```

For running tests:
```commandline
make test
```

For create admin user:
```commandline
make create-admin-user
```

## Notes:
* I used settlement checking (buy_from_exchange) asynchronously with celery task in every order creation.
* I used database row level locking for settlement checking and prevent race condition with skip locked rows in every task running.
* I used database row level locking and F object in django for updating balance value for each user
* I used authentication with Basic Auth