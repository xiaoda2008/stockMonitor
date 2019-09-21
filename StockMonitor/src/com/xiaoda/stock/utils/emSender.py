'''
Created on 2019年9月15日

@author: xiaoda
'''
import smtplib
from email.mime.text import MIMEText
from email.header import Header


class EmailSender(object):
    '''
    邮件发送器
    '''
    def __init__(self):
        '''
        Constructor
        '''
        


    def sendMails(self, mailSubject, mailContent):

        # 第三方 SMTP 服务
        mail_host="smtp.126.com"  #设置服务器
        mail_user="xiaoda2008"    #用户名
        mail_pass="PKUXiaoDa_001"   #口令 
         
         
        sender = 'xiaoda2008@126.com'
        receivers = ['xiaoda2008@126.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
         
        message = MIMEText(mailContent, 'plain', 'utf-8')
        message['From'] = Header("StockRobot")
        message['To'] =  Header("Xiaoda")


        message['Subject'] = Header(mailSubject, 'utf-8')
         
         
        try:
            smtpObj = smtplib.SMTP() 
            smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
            smtpObj.login(mail_user,mail_pass)  
            smtpObj.sendmail(sender, receivers, message.as_string())
            print("邮件发送成功：" + mailSubject + "\n" + mailContent)
        except smtplib.SMTPException:
            print("Error: 无法发送邮件")