#!/bin/bash

echo "backing up redmine"

mysqldump -u root -p111111 redmine | gzip > redmine_backup_$(date +%Y.%m.%d).sql.gz
