#!/usr/bin/python
# -*- coding: utf-8 -*-

from src.QcloudApi.modules.base import Base


class Live(Base):
    requestHost = 'live.api.qcloud.com'


def main():
    action = 'DescribeLVBOnlineUsers'
    config = {
        'Region': 'gz',
        'secretId': '',
        'secretKey': '',
        'method': 'get'
    }
    params = {}
    service = Live(config)
    print(service.call(action, params))

if __name__ == '__main__':
    main()
