#!/bin/bash

#* * * * *   /usr/bin/env > /home/username/tmp/cron-env
# run-as-cron /the/problematic/script --with arguments --and parameters
/usr/bin/env -i $(cat /tmp/cron-env) "$@"

