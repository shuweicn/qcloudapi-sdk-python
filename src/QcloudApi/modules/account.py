#!/usr/bin/python
# -*- coding: utf-8 -*-

from src.QcloudApi.modules.base import Base


class Account(Base):
    requestHost = 'account.api.qcloud.com'


def main():
    action = 'AddProject'
    config = {
        'Region': 'gz',
        'secretId': '',
        'secretKey': '',
        'method': 'get'
    }
    params = {}
    service = Account(config)
    print(service.call(action, params))

if __name__ == '__main__':
    main()
