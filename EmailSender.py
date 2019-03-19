# -*- coding: utf-8 -*-
#!/usr/bin/env python

import smtplib
from email.mime.text import MIMEText

class mailsender:
    def __init__(self):
        self.mail_host = 'smtp.163.com'
        self.mail_user = '*****@163.com'
        self.mail_password = '******'
        self.sender = '*****1@163.com'
        self.receivers = ['******@qq.com']

    def sendMsg(self, content, title):
        message = MIMEText(content, 'plain', 'utf-8')
        message['Subject'] = title
        message['From'] = self.sender
        message['To'] = self.receivers[0]

        try:
            # create a smtp object and connect with SSL
            smtpObj = smtplib.SMTP_SSL(self.mail_host)
            # login
            smtpObj.login(self.mail_user, self.mail_password)
            # send email
            smtpObj.sendmail(
                self.sender, self.receivers, message.as_string()
            )
            # quit
            smtpObj.quit()
            print('success')
        except smtplib.SMTPException as e:
            print('error', e)

def test():
    sender = mailsender()
    content = u"nba msg"
    sender.sendMsg(content, "nba")

if __name__ == "__main__":
    test()