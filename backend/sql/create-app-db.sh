#!/bin/bash

psql -U app_user -tc "SELECT 1 FROM pg_database WHERE datname = 'app'" | grep -q 1 || psql -U app_user -c "CREATE DATABASE app"
