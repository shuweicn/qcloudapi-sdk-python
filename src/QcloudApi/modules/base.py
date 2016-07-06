#!/usr/bin/python
# -*- coding: utf-8 -*-

import copy
import time
import random
import sys
import os
import warnings
from src.QcloudApi.common.request import Request

warnings.filterwarnings("ignore")

sys.path.append(os.path.split(os.path.realpath(__file__))[0] + os.sep + '..')


class Base:
    debug = 0
    requestHost = ''
    requestUri = '/v2/index.php'
    _params = {}

    def __init__(self, config):
        self.secret_id = config['secretId']
        self.secret_key = config['secretKey']
        self.default_region = config['Region']
        self.method = config['method']

    def _check_params(self, action, params):
        self._params = copy.deepcopy(params)
        self._params['Action'] = action[0].upper() + action[1:]

        if 'Region' not in self._params:
            self._params['Region'] = self.default_region

        if 'SecretId' not in self._params:
            self._params['SecretId'] = self.secret_id

        if 'Nonce' not in self._params:
            maxint = int((1 << 63) - 1)
            self._params['Nonce'] = random.randint(1, maxint)

        if 'Timestamp' not in self._params:
            self._params['Timestamp'] = int(time.time())

        return self._params

    def generate_url(self, action, params):
        self._check_params(action, params)
        request = Request(self.secret_id, self.secret_key)
        return request.generate_url(self.requestHost, self.requestUri,
                                    self._params, self.method)

    def call(self, action, params, files={}):
        self._check_params(action, params)
        request = Request(self.secret_id, self.secret_key)
        return request.send(self.requestHost, self.requestUri, self._params,
                            files, self.method, self.debug)


def main():
    action = 'DescribeUserInfo'
    config = {
        'Region': 'bj',
        'secretId': '',
        'secretKey': '',
        'method': 'get',
    }
    params = {
        'Nonce': random.randint(100000, 900000),
        'Timestamp': int(time.time())
    }
    base = Base(config)
    print(base.call(action, params))

if __name__ == '__main__':
    main()
