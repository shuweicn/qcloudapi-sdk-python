#!/usr/bin/python
# -*- coding: utf-8 -*-

from src.QcloudApi.modules.base import Base


class Cvm(Base):
    requestHost = 'cvm.api.qcloud.com'


def main():
    action = 'DescribeInstances'
    config = {
        'Region': 'bj',
        'secretId': '',
        'secretKey': '',
        'method': 'get'
    }
    params = {}
    service = Cvm(config)
    print(service.call(action, params))

if __name__ == '__main__':
    main()