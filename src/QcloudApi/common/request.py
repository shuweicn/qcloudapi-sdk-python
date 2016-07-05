#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib
import requests
from src.QcloudApi.common.sign import Sign
import random
import time


class Request:

    timeout = 10
    version = 'SDK_PYTHON_1.1'

    def __init__(self, secret_id, secret_key):
        self.secret_id = secret_id
        self.secret_key = secret_key

    def generate_url(self, request_host, request_uri, params, method='GET'):
        params['RequestClient'] = Request.version
        sign = Sign(self.secret_id, self.secret_key)
        params['Signature'] = sign.make(request_host, request_uri, params, method)
        params = urllib.parse.urlencode(params)

        url = 'https://%s%s' % (request_host, request_uri)
        if method.upper() == 'GET':
            url += '?' + params
        return url

    def send(self, request_host, request_uri, params, files={}, method='GET', debug=0):
        params['RequestClient'] = Request.version
        sign = Sign(self.secret_id, self.secret_key)
        params['Signature'] = sign.make(request_host, request_uri, params, method)

        url = 'https://%s%s' % (request_host, request_uri)

        if method.upper() == 'GET':
            req = requests.get(url, params=params, timeout=Request.timeout, verify=False)
            if debug:
                print('url:', req.url, '\n')
        else:
            req = requests.post(url, data=params, files=files, timeout=Request.timeout, verify=False)
            if debug:
                print('url:', req.url, '\n')

        if req.status_code != requests.codes.ok:
            req.raise_for_status()

        return req.text


def main():
    secret_id = ''
    secret_key = ''
    params = {
        'Action': 'DescribeUserInfo',
        'Nonce': random.randint(100000, 900000),
        'Region': 'bj',
        'SecretId': secret_id,
        'Timestamp': int(time.time()),
    }
    request = Request(secret_id, secret_key)
    print(request.generate_url('trade.api.qcloud.com', '/v2/index.php', params))
    # print(request.send('trade.api.qcloud.com', '/v2/index.php', params, debug=1))

if __name__ == '__main__':
    main()
