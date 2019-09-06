from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
import smtplib


#发件人
from_add = 'hejian@weather.com.cn'
#发送人密码
from_passwd = '123.coM'
#抄送人列表
# Cs = ['hejian@weather.com.cn','wuy@weather.com.cn','gaos@weather.com.cn','wuj@weather.com.cn']
#发送人列表
to_add = ['hejian@weather.com.cn']
smtp_server = 'smtp.exmail.qq.com'

def send_email(fj=None):
    m = MIMEMultipart()
    content = 'hello baidu.weather.com.cn'
    contentApart = MIMEText(content, _charset='utf-8')

    #发送附件
    if fj is not None:
        for i in fj:
            zipApart = MIMEApplication(open(i, 'rb').read())
            zipApart.add_header('Content-Disposition', 'attachment', filename=i)
            m.attach(zipApart)
            m.attach(contentApart)

    #邮件主题
    m['Subject'] = 'subject'
    #发件人
    m["From"] = 'hejian@weather.com.cn'
    #收件人
    m['To'] = ','.join(to_add)
    #邮件内容
    m.attach(contentApart)
    # 抄送
    # m['Cc'] = ",".join(Cs)

    try:
        server = smtplib.SMTP(smtp_server)
        server.login(from_add, from_passwd)
        server.sendmail(from_add,to_add,m.as_string())
        server.quit()
    except smtplib.SMTPException as error:
        print('Send error', error)

send_email()