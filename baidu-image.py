#-#- coding:utf-8 -#-
import requests
import time
import datetime
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
import os


hours = datetime.datetime.now()-datetime.timedelta(hours=1)
now = hours.strftime("%H:%M")
file_name = hours.strftime("%H")
years = time.strftime("%Y-%m-%d",time.localtime())
download_file_name = '2987893'+'_'+time.strftime('%Y%m%d',time.localtime())+file_name+'.zip'
DD_API='https://oapi.dingtalk.com/robot/send?access_token=2f77b6cfb480cb213779a1a10b0b78cd615778af07048406ff17eb9db8ad44c4'
headers = {'Content-Type': 'application/json;charset=utf-8'}
#发送人账号
from_add = 'hejian@weather.com.cn'
#发送人密码
from_passwd = '123.coM'
#抄送人列表
Cs = ['hejian@weather.com.cn','wuy@weather.com.cn','gaos@weather.com.cn','wuj@weather.com.cn']
#发送人列表
to_add = ['hejian@weather.com.cn']
smtp_server = 'smtp.exmail.qq.com'
taskID = '2987893'

def download_image(down_file):
    try:
        res = requests.get('http://dfeed.networkbench.com/rpc-export/exportScr.po?authkey=5BDfhrDnmd&taskId={0}&date={1}%20{2}'.format(taskID,years,now))
        if  res.headers['Content-Type'] == 'application/zip':
            with open(down_file,'ab') as imagefile:
                imagefile.write(res.content)
        else:
            print('%s %s not image'%(years,hours))
        res.close()
    except requests.HTTPError as e :
        print('wget failed',e)



def send_email(fj):
    m = MIMEMultipart()
    content = 'hello 各位领导，附件为baidu.weather.com.cn北京站点截图，请查收'
    contentApart = MIMEText(content, _charset='utf-8')

    for i in fj:
        zipApart = MIMEApplication(open(i, 'rb').read())
        zipApart.add_header('Content-Disposition', 'attachment', filename=i)
        m.attach(zipApart)
        m.attach(contentApart)

    m['Subject'] = '网页截图'
    m["From"] = 'hejian@weather.com.cn'
    m['To'] = ','.join(to_add)
    m['Cc'] = ",".join(Cs)

    try:
        server = smtplib.SMTP(smtp_server)
        server.login(from_add, from_passwd)
        server.sendmail(from_add,to_add+Cs,m.as_string())
        server.quit()
    except smtplib.SMTPException as error:
        print('Send error', error)

if __name__ == '__main__':
    now_time = time.strftime('%H',time.localtime())
    now_date = time.strftime('%Y-%m-%d',time.localtime())
    if now_time <= str(12):
        save_dir = '/ser/image/' + now_date + '/morning/'
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        if os.path.exists(save_dir + download_file_name):
            exit(10)
        else:
            download_image(save_dir + download_file_name)
    else:
        save_dir = '/ser/image/' + now_date + '/afternoon/'
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        if os.path.exists(save_dir + download_file_name):
            exit(10)
        else:
            download_image(save_dir + download_file_name)
    if now_time == str(12):
        fl = os.listdir(save_dir)
        os.chdir(save_dir)
        send_email(fl)
    if now_time == str(17):
        fl = os.listdir(save_dir)
        os.chdir(save_dir)
        send_email(fl)
