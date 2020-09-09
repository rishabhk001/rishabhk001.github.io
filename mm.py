
import requests
import json
import random
#from tkinter import *
#from tkinter.messagebox import*
def send_SMS(no,msg):
  url = 'https://www.fast2sms.com/dev/bulk'
  param = {
    'authorization': 'V0XUphMyGqrkLNnD4Sw83CAQmteiRaWZJO7bdT1sP9Hv25IlFoENq8XIkRYJ7PUV2MHumrF4vdQc5gO0',
    'sender_id': 'FSTSMS',
    'message': msg,
    'route': 'p',
    'numbers': no,
    'language': 'english'
  }
  response = requests.get(url,params=param)
  dic = response.json()
  print(dic)
otp=random.randint(1000,9999)
msg="Your OTP is : "+str(otp)
send_SMS('7417680837',msg)