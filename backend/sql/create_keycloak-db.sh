#!/bin/bash

psql -U app_user -tc "SELECT 1 FROM pg_database WHERE datname = 'keycloak'" | grep -q 1 || psql -U app_user -c "CREATE DATABASE keycloak"

psql -U app_user -c "CREATE USER keycloak WITH PASSWORD 'kc'"
