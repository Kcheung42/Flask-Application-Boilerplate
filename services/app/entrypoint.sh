#!/bin/sh

echo "Waiting for postgres..."

# So, we referenced the Postgres container using the name of the service, app-db.
# The loop continues until something like:
# Connection to app-db port 5432 [tcp/postgresql] succeeded! is returned.

while ! nc -z app-db 5432; do
    sleep 0.1
done

echo "PostgreSQL started"

python manage.py run -h 0.0.0.0
