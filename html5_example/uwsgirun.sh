#!/bin/bash

#uwsgi --socket 127.0.0.1:3031 -w flask-hw
#uwsgi --http :8000 --module flaskhw --callable app
uwsgi --socket 127.0.0.1:3031 --module flaskhw --callable app
