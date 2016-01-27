#!/usr/bin/env python2

"""
Service manager
"""

import argparse
from pprint import pprint
import sys
import os
import logging
from subprocess import check_output, CalledProcessError

__version__ = 'v0.21'

SERVICES = {
    'car_rec': {
        'description': 'Avito offline cars recommendations',
        'log_location': '/var/local/recom/car_rec.log',
        'directory': '/var/local/crm/avito-recommendations/research/cars_recommendations/carsrec',
        'executable': 'car_rec_runner.py',
    },
    'job_rec': {
        'description': 'Avito offline job recommendations',
        'log_location': '//job_rec.log',
        'directory': '/var/local/crm/avito-recommendations/research/job_recommendations',
        'executable': 'job_rec_runner.py',
    },
    'dummy': {
        'description': 'Sample service',
        'log_location': '/tmp/dummy.log',
        'directory': '/tmp/',
        'executable': 'dummy.py',
    }
}


class Settings(object):
    history_location = '/var/local/bi_service/history'
    logger = 'bi.service.history'


def parse_args():
    """ Process command line arguments. """
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', "--service_name", type=str, required=False)
    parser.add_argument('-S', "--status-all", action='store_true',
                        required=False, help='print all services status.')
    parser.add_argument('-c', "--command", type=str, required=False)
    parser.add_argument('-H', "--history", action='store_true', required=False,
                        help='Print bi.service log', )
    parser.add_argument('--version', action='version',
                        version='{} {}'.format(__name__, __version__))
    parser.add_argument('-l', '--list', action='store_true',
                        help='Show brief information about available services')
    parser.add_argument('--full_list', action='store_true',
                        help='Show all information about services')
    parser.add_argument('service_', nargs='?', default='')
    parser.add_argument('command_', nargs='?', default='')
    args = parser.parse_args()
    return args



def config_history_logger(settings):
    logger = logging.getLogger(settings.logger)
    logger.handlers = []
    logger.setLevel(logging.INFO)
    file_channel = logging.FileHandler(settings.history_location)
    formatter = logging.Formatter('[%(asctime)s] %(message)s')
    file_channel.setFormatter(formatter)
    logger.addHandler(file_channel)
    return logger


def get_service_status(serv_name):
    service_desc = SERVICES[serv_name]
    checker = 'pgrep -c -f {}'.format(service_desc['executable'])
    pids = check_output(checker, shell=True)
    if int(pids) < 2:
        print('not running')
    else:
        print('process number : {}'.format(int(pids) - 1))
    os.system('tail -n4 {}'.format(service_desc['log_location']))


def service_command(service_name, command):
    settings = Settings()
    hist_logger = config_history_logger(settings)
    if service_name not in SERVICES:
        print('no such service :-(')
        sys.exit(0)
    service_desc = SERVICES[service_name]
    if command == 'log':
        os.system('tail -n100 -f {}'.format(service_desc['log_location']))
    elif command == 'status':
        get_service_status(service_name)
        sys.exit(0)
    elif command == 'kill':
        checker = 'pgrep -c -f {}'.format(service_desc['executable'])
        proc_number = check_output(checker, shell=True)
        if int(proc_number) < 2:
            print('Process wasn\'t running, nothing to do.')
        else:
            hist_logger.info('{} {}'.format(service_name, command))
            killer = 'pkill -f {}'.format(service_desc['executable'])
            try:
                check_output(killer, shell=True)
            except CalledProcessError:
                print('Killed {} processes'.format(int(proc_number) - 1))
                pass
            else:
                print('Killed {} processes'.format(int(proc_number) - 1))

    else:
        os.chdir(service_desc['directory'])
        command = './{} {}'.format(service_desc['executable'],
                                   command)
        run_command = (
            'export PYTHONIOENCODING=utf-8 && nohup '
            '{} > /tmp/bi_service_out_{} 2>&1 &').format(
            command, service_desc['executable'])
        #print(run_command)
        err_code = os.system(run_command)
        hist_logger.info(command)
        if err_code:
            hist_logger.error('got error during {}'.format(command))
        else:
            print("Command accepted. See out in /tmp/bi_service_out_{}".format(
                service_desc['executable']))


def main():
    """ """
    args = parse_args()
    if args.list:
        for serv_name in SERVICES:
            print(serv_name)
    elif args.history:
        settings = Settings()
        with open(settings.history_location) as hist_fd:
            print(hist_fd.read())
    elif args.full_list:
        for serv_name in SERVICES:
            print('--')
            print(serv_name)
            get_service_status(serv_name)
    elif args.service_name:
        service_command(args.service_name, args.command)
    elif args.service_:
        service_command(args.service_, args.command_)


if __name__ == '__main__':
    main()