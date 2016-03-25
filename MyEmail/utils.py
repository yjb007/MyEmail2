#!/usr/bin/env python
# encoding: utf-8

import yaml
import argparse
from  exceptions import ConfigError,OptionReq
from MyEmail import myEmail

#从SMTP服务器的配置文件中load出一个字典，放到新的字典ret中准备被调用
#返回的是一个字典ret
#get配置文件
def getConfig(config_file,section):
    ret = {
        'result':True,
        'comment':[],
        'options':{},
    }
    try:
        with open(config_file, 'rb') as f:
            config = yaml.load(f)
            ret['options'] = config[section]
    except Exception, e:
        ret['result'] = False
        ret['comment'].append(str(e))
        return ret
    return ret



#检查SMTP服务器的参数配置是否为空
#返回的是一个字典ret
#检查配置文件
def checkConfig(options,requisit_opts):
    ret = {
        'result': True,
        'comment': [],
    }

    for eachopt in requisit_opts:
        if not options.has_key(eachopt):
            ret['result'] = False
            ret['comment'].append('%s option is requisite' %(eachopt))
    return ret


#找出自己需要的配置文件
def getOptions(config_file, section, requisit_opts):
    config = getConfig(config_file, section)
    if not config['result']:
        raise ConfigError(';'.join(config['comment']))
    options = config['options']
    config_check = checkConfig(options, requisit_opts)
    if not config_check['result']:
        raise OptionReq(';'.join(config_check['comment']))
    return options

def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('to', help='send to somebody')
    parser.add_argument('subject', help='subject')
    parser.add_argument('message', help='message')
    args = parser.parse_args()
    to = args.to
    subject = args.subject
    message = args.message
    return (to,subject,message)


def Email(config_file, __config_section__, __requisit_opts__, myEmail):
    to, subject, message = getArgs()
    options = getOptions(config_file, __config_section__, __requisit_opts__)
    ret = myEmail(options).sendEmail(to, subject, message)
    return ret











