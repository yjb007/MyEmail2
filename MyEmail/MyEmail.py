#!/usr/bin/env python
# encoding: utf-8

import smtplib
from socket import timeout
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class myEmail(object):
    def __init__(self, options):
        self.options = options
    # options是一个字典dict
    def sendEmail(self,to,subject,message):
        ret = {
            "result": True,
            "comment": [],
        }
        smtp_host = self.options['smtp_host']
        smtp_user = self.options['smtp_user']
        smtp_password = self.options['smtp_password']
        smtp_tls = self.options.get('smtp_tls', False)
        if smtp_tls:
            smtp_port = int(self.options.get('smtp_port', 465))
            server = smtplib.SMTP_SSL()
        else:
            smtp_port = int(self.options.get('smtp_port', 25))
            server = smtplib.SMTP()

        #构造邮件
        msg = MIMEMultipart()
        content = MIMEText(message, _subtype='html', _charset='utf-8')
        msg.attach(content)
        msg['To'] = to
        msg['from'] = '%s<%s>' %(smtp_user, smtp_user)
        msg['subject'] = subject

        try:
            server.connect(smtp_host, smtp_port)
        except timeout:
            ret['result'] = False
            ret['comment'].append('%s connect timeout' %(smtp_host))

        if smtp_password:
            try:
                server.login(smtp_user, smtp_password)
            except Exception, e:
                ret['result'] = False
                ret['comment'].append(str(e))
                return ret

        try:
            server.sendmail(smtp_user, to, msg.as_string())
            server.quit()
        except Exception, e:
            ret['result'] = False
            ret['comment'].append(str(e))
            return ret


        ret['comment'].append('send mail success!')
        return ret









