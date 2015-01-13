#!/bin/bash

echo "Extracting redmine backup $1 ..."

zcat $1 | mysql -u root -p111111 redmine
