#!/usr/bin/python
# -*- coding: utf-8 -*-
import hashlib
import os
from src.QcloudApi.modules.base import Base


class Cdn(Base):
    requestHost = 'cdn.api.qcloud.com'

    def upload_cdn_entity(self, params):
        action = 'UploadCdnEntity'
        if not params.get('entityFile'):        # == None
            raise ValueError('entityFile can not be empty.')
        if os.path.isfile(params['entityFile'] == False):
            raise ValueError('entityFile is not exist.')

        file = params.pop('entityFile')
        if 'entityFileMd5' not in params:
            params['entityFileMd5'] = hashlib.md5(open(file, 'rb').read()).hexdigest()

        files = {
            'entityFile': open(file, 'rb')
        }

        return self.call(action, params, files)


def main():
    config = {
        'Region': 'gz',
        'secretId': '',
        'secretKey': '',
        'method': 'post'
    }
    params = {
        'entityFileName': './/test.txt',
        'entityFile': './/test.txt'
    }
    service = Cdn(config)
    print(service.upload_cdn_entity(params))

if __name__ == '__main__':
    main()
