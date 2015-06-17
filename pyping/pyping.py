#!/usr/bin/env python3
import os
import sys
import time
import argparse

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def ping(ip_addr):
    """ Return True if server is up. """
    response = os.system("ping -W 1 -c 1 " + ip_addr + ' > /dev/null')
    return not bool(response)


def pingloop(ip_addr):
    """ Continuously ping given ip addr. """

    cur_time = last_time = time.time()
    uptime = 0
    downtime = 0
    up_interval = 0
    last_state = False
    while True:
        res = ping(ip_addr)
        cur_time = time.time()
        if res:
            uptime += cur_time - last_time
            out = 'UP'
            color = bcolors.OKGREEN + bcolors.BOLD
            if last_state:
                up_interval += cur_time - last_time
            last_state = True
        else:
            out = 'DOWN'
            downtime += cur_time - last_time
            color = bcolors.FAIL + bcolors.BOLD
            last_state = False
            up_interval = 0
        last_time = cur_time
        total_time = uptime + downtime
        up_perc = round((uptime/total_time) * 100, 2)
        down_perc = round((downtime/total_time) * 100, 2)
        sys.stdout.write("\r{}{}{}, interval {}, uptime: {} ({} %), downtime: {} ({} %)".format(
            color, out, bcolors.ENDC, human_readable_time(up_interval), human_readable_time(uptime), up_perc, human_readable_time(downtime), down_perc))
        time.sleep(1)


def human_readable_time(sec):
    """ Return string n hours, n mins, n sec from sec. """
    date = ''
    mins = int(sec / 60)
    if not mins:
        return '{}s'.format(int(sec)) 
    hours = int(mins / 60)
    if not hours:
        return '{}m {}s'.format(mins, int(sec - mins*60)) 
    return '{}h {}m {}s'.format(hours, mins - hours*60, int(sec - mins*60 - hours*60*60)) 


def parse_args():
    """ Process command line arguments. """
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--ip_addr", type=str,
                        default='8.8.8.8',
                        help="ip addr")
    args = parser.parse_args()
    return args


def main():
    """ """
    args = parse_args()
    pingloop(args.ip_addr)


if __name__ == '__main__':
    main()


