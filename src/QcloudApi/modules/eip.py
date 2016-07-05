#!/usr/bin/python
# -*- coding: utf-8 -*-

from src.QcloudApi.modules.base import Base


class Eip(Base):
    requestHost = 'eip.api.qcloud.com'


def main():
    action = 'DescribeEip'
    config = {
        'Region': 'gz',
        'secretId': '',
        'secretKey': '',
        'method': 'get'
    }
    params = {}
    service = Eip(config)
    print(service.call(action, params))

if __name__ == '__main__':
    main()
