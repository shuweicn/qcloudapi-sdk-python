#!/usr/bin/python
# -*- coding: utf-8 -*-

from src.QcloudApi.modules.base import Base


class Snapshot(Base):
    requestHost = 'snapshot.api.qcloud.com'


def main():
    action = 'DescribeSnapshots'
    config = {
        'Region': 'gz',
        'secretId': '',
        'secretKey': '',
        'method': 'get'
    }
    params = {}
    service = Snapshot(config)
    print(service.call(action, params))

if __name__ == '__main__':
    main()