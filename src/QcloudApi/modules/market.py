#!/usr/bin/python
# -*- coding: utf-8 -*-

from src.QcloudApi.modules.base import Base


class Market(Base):
    requestHost = 'market.api.qcloud.com'


def main():
    action = 'QueryVoucherData'
    config = {
        'Region': 'gz',
        'secretId': '',
        'secretKey': '',
        'method': 'get'
    }
    params = {}
    service = Market(config)
    print(service.call(action, params))

if __name__ == '__main__':
    main()
