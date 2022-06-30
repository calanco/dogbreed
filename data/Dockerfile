FROM postgres:14

EXPOSE 5432

ENV POSTGRES_USER=docker
ENV POSTGRES_PASSWORD=docker

COPY init.sql /docker-entrypoint-initdb.d/