#!/usr/bin/python
# -*- coding: utf-8 -*-

from src.QcloudApi.modules.base import Base


class Yunsou(Base):
    requestHost = 'yunsou.api.qcloud.com'


def main():
    action = 'DataSearch'
    config = {
        'Region': 'gz',
        'secretId': '',
        'secretKey': '',
        'method': 'get'
    }
    params = {
        "appId" : "123",
        "search_query": "qq",
        "page_id": 0,
        "num_per_page": 10,
    }
    service = Yunsou(config)
    print(service.call(action, params))

if __name__ == '__main__':
    main()
