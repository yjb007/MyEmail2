#!/usr/bin/env python
# encoding: utf-8

import os
from MyEmail.utils import Email
from MyEmail.MyEmail import myEmail
from MyEmail.exceptions import NotifyError
from MyEmail.utils import getConfig

__config_section__ = 'SMTP'
__requisit_opts__ = ['smtp_host','smtp_user']




if __name__ == '__main__':
    config_file = 'config.yaml'
    config_file = os.path.dirname(os.path.realpath(__file__)) + os.sep + config_file
    ret = Email(config_file, __config_section__, __requisit_opts__, myEmail)

    if not ret['result']:
        raise NotifyError(';'.join(ret['comment']))
    else:
        print ';'.join(ret['comment'])

