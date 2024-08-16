#!/bin/sh

export PG_USER="postgres"

psql productstore -c "CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\";"
