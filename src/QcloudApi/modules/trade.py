#!/usr/bin/python
# -*- coding: utf-8 -*-

from src.QcloudApi.modules.base import Base


class Trade(Base):
    requestHost = 'trade.api.qcloud.com'


def main():
    action = 'DescribeUserInfo'
    config = {
        'Region': 'bj',
        'secretId': '',
        'secretKey': '',
        'method': 'get'
    }
    params = {}
    service = Trade(config)
    print(service.call(action, params))

if __name__ == '__main__':
    main()