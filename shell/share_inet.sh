#!/bin/bash

# run on server

iptables -t nat -A POSTROUTING -o wlan0 -j MASQUERADE

route add -net 10.0.0.0 netmask 255.255.255.0 dev eth0
route add -net 0.0.0.0 netmask 0.0.0.0 dev wlan0
