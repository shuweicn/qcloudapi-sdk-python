#!/usr/bin/python
# -*- coding: utf-8 -*-


class QcloudApi:
    def __init__(self, module, config):
        self.module = module
        self.config = config

    def __factory(self, module, config):
        if module == 'cdb':
            from src.QcloudApi.modules.cdb import Cdb
            service = Cdb(config)
        elif module == 'account':
            from src.QcloudApi.modules.account import Account
            service = Account(config)
        elif module == 'cvm':
            from src.QcloudApi.modules.cvm import Cvm
            service = Cvm(config)
        elif module == 'image':
            from src.QcloudApi.modules.image import Image
            service = Image(config)
        elif module == 'lb':
            from src.QcloudApi.modules.lb import Lb
            service = Lb(config)
        elif module == 'sec':
            from src.QcloudApi.modules.sec import Sec
            service = Sec(config)
        elif module == 'trade':
            from src.QcloudApi.modules.trade import Trade
            service = Trade(config)
        elif module == 'bill':
            from src.QcloudApi.modules.bill import Bill
            service = Bill(config)
        elif module == 'monitor':
            from src.QcloudApi.modules.monitor import Monitor
            service = Monitor(config)
        elif module == 'cdn':
            from src.QcloudApi.modules.cdn import Cdn
            service = Cdn(config)
        elif module == 'vpc':
            from src.QcloudApi.modules.vpc import Vpc
            service = Vpc(config)
        elif module == 'vod':
            from src.QcloudApi.modules.vod import Vod
            service = Vod(config)
        elif module == 'yunsou':
            from src.QcloudApi.modules.yunsou import Yunsou
            service = Yunsou(config)
        elif module == 'wenzhi':
            from src.QcloudApi.modules.wenzhi import Wenzhi
            service = Wenzhi(config)
        elif module == 'market':
            from src.QcloudApi.modules.market import Market
            service = Market(config)
        elif module == 'live':
            from src.QcloudApi.modules.live import Live
            service = Live(config)
        elif module == 'eip':
            from src.QcloudApi.modules.eip import Eip
            service = Eip(config)
        elif module == 'cbs':
            from src.QcloudApi.modules.cbs import Cbs
            service = Cbs(config)
        elif module == 'snapshot':
            from src.QcloudApi.modules.snapshot import Snapshot
            service = Snapshot(config)
        elif module == 'scaling':
            from src.QcloudApi.modules.scaling import Scaling
            service = Scaling(config)
        else:
            raise ValueError('module not exists')

        return service

    def set_secret_id(self, secret_id):
        self.config['secretId'] = secret_id

    def set_secret_key(self, secret_key):
        self.config['secretKey'] = secret_key

    def set_request_method(self, method):
        self.config['method'] = method

    def set_region(self, region):
        self.config['region'] = region

    def generate_url(self, action, params):
        service = self.__factory(self.module, self.config)
        return service.generate_url(action, params)

    def call(self, action, params):
        service = self.__factory(self.module, self.config)
        methods = dir(service)
        for method in methods:
            if method == action:
                func = getattr(service, action)
                return func(params)

        return service.call(action, params)


def main():
    module = 'trade'
    action = 'DescribeUserInfo'
    config = {
        'Region': 'bj',
        'secretId': '',
        'secretKey': '',
        'method': 'get'
    }
    params = {}
    service = QcloudApi(module, config)
    print('URL:\n' + service.generate_url(action, params))
    print(service.call(action, params))

if __name__ == '__main__':
    main()
