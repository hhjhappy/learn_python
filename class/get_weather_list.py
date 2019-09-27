import requests
import datetime
from hashlib import sha256
from urllib import parse
import hmac
import base64


username = 'tq121'
apiKey = 'si8wJnCcKCmSE6wsHhmg'
post_url = 'https://open.chinanetcenter.com/api/domain'

def getDate():
    GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
    date_gmt = datetime.datetime.utcnow().strftime(GMT_FORMAT)
    return date_gmt

def getAuth(userName, apikey, date):
    signed_apikey = hmac.new(apikey.encode('utf-8'), date.encode('utf-8'), sha256).digest()
    signed_apikey = base64.b64encode(signed_apikey)
    signed_apikey = userName + ":" + signed_apikey.decode()
    signed_apikey = base64.b64encode(signed_apikey.encode('utf-8'))
    return signed_apikey

key = getAuth(username,apiKey,getDate())
# print(key)

def createHeader(authStr,date):
    headers = {
    'Date': date,
    'Accept': 'application/json',
    'Content-type': 'application/json',
    'Authorization': 'Basic ' + authStr.decode()
    }
    return headers

r = requests.get(url = post_url,headers=createHeader(key,getDate()))
# print(r.text)
for i in r.json():
    print(i)
# print(r.json())