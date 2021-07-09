# pull official base image
FROM postgres:13-alpine

# This file will execute on init
ADD create.sql /docker-entrypoint-initdb.d
