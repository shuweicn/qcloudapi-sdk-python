#!/usr/bin/python
# -*- coding: utf-8 -*-

from src.QcloudApi.modules.base import Base


class Lb(Base):
    requestHost = 'lb.api.qcloud.com'


def main():
    action = 'DescribeLoadBalancers'
    config = {
        'Region': 'gz',
        'secretId': '',
        'secretKey': '',
        'method': 'get'
    }
    params = {}
    service = Lb(config)
    print(service.call(action, params))

if __name__ == '__main__':
    main()