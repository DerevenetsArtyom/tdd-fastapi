#!/bin/sh

echo "Waiting for postgres..."

while ! nc -z database 5432; do
  sleep 0.5
done

echo "PostgreSQL started"

exec "$@"
