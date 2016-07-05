#!/usr/bin/python
# -*- coding: utf-8 -*-

from src.QcloudApi.modules.base import Base


class Bill(Base):
    requestHost = 'bill.api.qcloud.com'


def main():
    action = 'DescribeBills'
    config = {
        'Region': 'gz',
        'secretId': '',
        'secretKey': '',
        'method': 'get'
    }
    params = {}
    service = Bill(config)
    print(service.call(action, params))

if __name__ == '__main__':
    main()
