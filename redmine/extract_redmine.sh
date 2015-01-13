#!/bin/bash

echo "Extracting redmine backup $1 ..."

mysql -u root -p111111 -e 'create database if not exists redmine;'
zcat $1 | mysql -u root -p111111 redmine
