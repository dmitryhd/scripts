#!/usr/bin/python
#-*- coding: utf-8 -*-

import os

from time import gmtime, strftime
source_dirs = ['/etc', '/boot', '/home', '/lib', '/lib64', '/opt', '/root', '/run', '/sbin', '/bin', '/selinux', '/srv', '/usr', '/var']
#source_dirs = ['/opt']
backup_dir = '/tmp/backups'

task_name = 'full_system_backup_' + strftime("%Y_%m_%d_%H_%M_%S", gmtime())
print('backing up file: ' + task_name)
target_dir = os.path.join(backup_dir, task_name)

if not os.path.exists(target_dir):
    os.makedirs(target_dir)

for directory in source_dirs:
    print('backing up ' + directory + ' ...')
    os.system('cp -rp ' + directory + ' ' + target_dir)

os.chdir(backup_dir)
os.system('tar czf ' + task_name + '.tgz ' + task_name)
os.system('rm -rf ' + task_name)

suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
def humansize(nbytes):
    if nbytes == 0: return '0 B' 
    i = 0
    while nbytes >= 1024 and i < len(suffixes)-1:
        nbytes /= 1024.
        i += 1
    f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
    return '%s %s' % (f, suffixes[i])

file_size = humansize(os.stat(task_name + '.tgz').st_size)

print('=====')
print('created file {} size: {}'.format(task_name, file_size))

