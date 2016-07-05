#!/usr/bin/python
# -*- coding: utf-8 -*-

from src.QcloudApi.modules.base import Base


class Wenzhi(Base):
    requestHost = 'wenzhi.api.qcloud.com'


def main():
    action = 'TextSentiment'
    config = {
        'Region': 'gz',
        'secretId': '',
        'secretKey': '',
        'method': 'get'
    }
    params = {
        "content" : "123",
    }
    service = Wenzhi(config)
    print(service.call(action, params))

if __name__ == '__main__':
    main()
