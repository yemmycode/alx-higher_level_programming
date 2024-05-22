#!/bin/bash

MYSQL_USER="your_mysql_username"
MYSQL_PASSWORD="your_mysql_password"

CREATE_DB_QUERY="CREATE DATABASE IF NOT EXISTS hbtn_0c_0;"

mysql -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "$CREATE_DB_QUERY"
