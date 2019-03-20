# -*- coding: utf-8 -*-
# !/usr/bin/env python

import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


class mailsender:
    def __init__(self):
        self.mail_host = 'smtp.gmail.com'
        self.mail_user = 'wlc.9424@gmail.com'
        self.mail_password = 'jkhonssyfmcnfuly'
        self.sender = 'wlc.9424@gmail.com'
        self.receivers = ['wanglic@oregonstate.edu']

    def sendMsg(self, content, image, title):
        message = MIMEMultipart('related')
        message['Subject'] = title
        message['From'] = self.sender
        message['To'] = self.receivers[0]
        text = MIMEText(content, 'plain', 'utf-8')
        message.attach(text)
        file = open(image, "rb")
        img_data = file.read()
        file.close()
        img = MIMEImage(img_data)
        img.add_header('Content-ID', 'dns_config')
        message.attach(img)

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
