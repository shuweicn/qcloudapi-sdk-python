#!/usr/bin/python
# -*- coding: utf-8 -*-

import binascii
import hashlib
import hmac


class Sign:
    def __init__(self, secret_id, secret_key):
        self.secret_id = secret_id
        self.secret_key = secret_key

    def make(self, request_host, request_uri, params, method='GET'):
        arg = {}
        for param_key in params:
            if method == 'post' and str(params[param_key])[0:1] == "@":
                continue
            arg[param_key] = params[param_key]

        get_arg = "&".join(
            [k.replace("_",".")+"="+str(arg[k]) for k in sorted(arg.keys())]
        )

        url = method.upper() + request_host + request_uri + '?' + get_arg
        byte_secret_key = bytes(self.secret_key, 'utf-8')
        byte_url = bytes(url, 'utf-8')
        hashed = hmac.new(byte_secret_key, byte_url, hashlib.sha1)
        return binascii.b2a_base64(hashed.digest()).strip()


def main():
    secret_id = ''
    secret_key = ''

    params = {
        'Action': 'DescribeInstances',
        'Nonce': 10086,
        'Region': 'bj',
        'SecretId': secret_id,
        'Timestamp': 321656535,
        'instanceIds.0': 'ins-09dx96dg',
        'limit': 20,
        'offset': 0,
    }
    sign = Sign(secret_id, secret_key)
    print(sign.make('cvm.api.qcloud.com', '/v2/index.php', params))

if __name__ == '__main__':
    main()
