#!/usr/bin/python
# -*- coding: utf-8 -*-

from src.QcloudApi.qcloudapi import QcloudApi

module = 'cvm'
action = 'DescribeInstances'
config = {
    'Region': 'gz',
    'secretId': '',
    'secretKey': '',
    'method': 'post'
}
params = {

}
try:
    service = QcloudApi(module, config)
    print(service.generate_url(action, params))
    print(service.call(action, params))
    # service.setRequestMethod('get')
    # print(service.call('DescribeCdnEntities', {}))
except Exception as e:
    print('exception:', e)
