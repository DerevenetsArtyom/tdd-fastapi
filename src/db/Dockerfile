# pull official base image
FROM postgres:14-alpine

# This file will execute on init
ADD create.sql /docker-entrypoint-initdb.d
