#!/bin/bash

backup_folder="/home/backup/"
end_folder="work-backup"
rsync -aAXv --exclude={"/dev/*","/proc/*","/sys/*","/tmp/*","/run/*","/mnt/*","/media/*","/lost+found","$backup_folder"} /* $backup_folder$end_folder

