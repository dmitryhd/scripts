#!/usr/bin/env python3

import unittest
import sys
import subprocess


def ssh_get(ip_addr, username, password, command):
    res = subprocess.check_output(
        'sshpass -p{} ssh {}@{} -t "{}" 2> /dev/null'.format(password,
                                                             username,
                                                             ip_addr,
                                                             command),
         shell=True)
    res = res.decode('utf8')
    return res.strip()


class GpuManager:
    USERNAME = 'root'
    PASSWORD = '111111'
    def __init__(self, name, ip_addr):
        self.name = name
        self.ip_addr = ip_addr
        self.gpu_get_temp_command = 'DISPLAY=:0 aticonfig --odgt --adapter=all'
        self.gpu_get_load_command = 'DISPLAY=:0 aticonfig --odgc --adapter=all'

    def get_state_all(self):
        gpu_temperature = ssh_get(self.ip_addr, self.USERNAME,
                                  self.PASSWORD, self.gpu_get_temp_command)
        return gpu_temperature


class TestGetGpuState(unittest.TestCase):
    TEST_SERVER_IP = '10.0.0.57'
    USERNAME = 'user'
    PASSWORD = '111111'
    ECHO_COMM = 'echo 555'

    def test_get_all_gpu_state(self):
        gpu_manager = GpuManager('gpu_serv', self.TEST_SERVER_IP)
        state = gpu_manager.get_state_all()
        assert state, 'No output'
        assert len(state) == 4, 'Wrong state: {}'.format(state)

    def test_ssh_get(self):
        echo = ssh_get(self.TEST_SERVER_IP, self.USERNAME,
                       self.PASSWORD, self.ECHO_COMM)
        assert echo == '555', 'got {}'.format(echo)


def main():
    if sys.argv[1] == '-v':
        unittest.main()


if __name__ == '__main__':
    main()
