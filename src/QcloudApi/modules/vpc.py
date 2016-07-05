#!/usr/bin/python
# -*- coding: utf-8 -*-

from src.QcloudApi.modules.base import Base


class Vpc(Base):
    requestHost = 'vpc.api.qcloud.com'


def main():
    action = 'DescribeVpcs'
    config = {
        'Region': 'gz',
        'secretId': '',
        'secretKey': '',
        'method': 'get'
    }
    params = {}
    service = Vpc(config)
    print(service.call(action, params))

if __name__ == '__main__':
    main()
