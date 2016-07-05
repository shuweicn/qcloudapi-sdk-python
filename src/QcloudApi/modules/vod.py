#!/usr/bin/python
# -*- coding: utf-8 -*-

from src.QcloudApi.modules.base import Base


class Vod(Base):
    requestHost = 'vod.api.qcloud.com'


def main():
    action = 'DescribeVodPlayUrls'
    config = {
        'Region': 'gz',
        'secretId': '',
        'secretKey': '',
        'method': 'get'
    }
    params = {}
    service = Vod(config)
    print(service.call(action, params))

if __name__ == '__main__':
    main()