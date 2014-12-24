#!/bin/bash
cd /usr/share/redmine
sudo ruby script/rails server webrick -e production
