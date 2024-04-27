
# Encoding: utf-8
# Decode by Plya Team - DecodeX
# Copyright: Plya - Team
# Follow Us On Telegram [ @Plya_Team ]   	

import requests
import random
import requests
import json
import pyfiglet
import sys
import time
import os
import uuid
import webbrowser
import fake_useragent
import datetime  # Import datetime module for date manipulation



Ab = '\033[1;92m'
aB = '\033[1;91m'
AB = '\033[1;96m'
aBbs = '\033[1;93m'
AbBs = '\033[1;95m'
A_bSa = '\033[1;31m'
a_bSa = '\033[1;32m'
faB_s = '\033[2;32m'
a_aB_s = '\033[2;39m'
Ba_bS = '\033[2;36m'
Ya_Bs = '\033[1;34m'
S_aBs = '\033[1;33m'
ab = pyfiglet.figlet_format("SafeUm")
print(a_bSa + ab)


def to(s):
    for char in s + "\n":
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(500.0 / 8000)


to(
    f"\033[31;m TOOL >> \033[1;36mACCOUNT CREATOR\n\033[1;31m DEVELOPER >>\033[1;33m @Theyhates_joker\n\033[31;m")
print('')
print('\033[32;m')

from os import system, name
from ssl import CERT_NONE
from gzip import decompress
from random import choice, choices
from concurrent.futures import ThreadPoolExecutor
from json import dumps

try:
    from websocket import create_connection
except:
    system('pip install websocket-client')
    from websocket import create_connection

failed = 0
success = 0
retry = 0
accounts = []

# Expiry date
expiry_date = datetime.datetime(2074, 4, 18)

def work():
    global failed, success, retry
    username = choice('qwertyuiooasdfghjklzxcvpbnm') + ''.join(choices(list('qwertyuioasdfghjklzxcvbnpm1234567890'), k=22))
    # Check if the current date is past the expiry date
    if datetime.datetime.now() > expiry_date:
        print("Script expired")
        return
        
    try:
        con = create_connection("wss://195.13.182.213/Auth",
                                header={"app": "com.safeum.android", "host": None, "remoteIp": "195.13.182.213",
                                        "remotePort": str(8080), "sessionId": "b6cbb22d-06ca-41ff-8fda-c0ddeb148195",
                                        "time": "2024-04-11 11:00:00", "url": "wss://51.79.208.190/Auth"},
                                sslopt={"cert_reqs": CERT_NONE})
        con.send(dumps(
          {"action":"Register","subaction":"Desktop","locale":"en_LV","gmt":"+03","password":{"m1x":"5284472cbfadaf07932442855c56c53eefa7a3ba3e5df71908c299edc1141649","m1y":"bd36a298d03c9d8f637895bc4595d7fffb445ebde10226b5f4f7e8b5ba0bd853","m2":"b387c7efe18b119459a00c055bd87405d833e4a804ee10495a5f1535d42b5c29","iv":"3205f0d29dd638d12f8ab293c2fd46ac","message":"2b177cd8cafc75d2fb0735a11190c6b893a681ec188120fba2323d22a58d3d374440f6b84985d1787639103521d0ad8fc1c94b9e398b227caec4634d20aa8dbd9d38ded1289a0b01db1fc8e2f0292617"},"magicword":{"m1x":"370c2ed52f368efb131857b7132d78cdf687a88210fd91f9d24455d30de15256","m1y":"b081644eaad191729fec40d8ec401ec49d0a38c488f3de10d374f2e9f6257679","m2":"090e58d2cabe8bc66c7ca3afa48b032545e8aca522431881cf0c8643b7c4fbcc","iv":"b706987a9c3bd72369b135bbd0421a75","message":"b2da38580a855ed6592b6b95a50e712e"},"magicwordhint":"0000","login":str(username),"devicename":"Xiaomi 23106RN0DA","softwareversion":"1.1.0.2300","nickname":"joag339nfa","os":"AND","deviceuid":"7796efb323b2256e","devicepushuid":"*djLCF_YCTyKYwPG2sfCouM:APA91bF414Dk4qM3A9R7zaK6qQr_LKS8VkXs9zkgUAdNQJnLoQM4rpZwzv6kTI5U0Ud5SitNNXRYdL53FjHzfKgl_g19gyxqZWkZhFptvoJ3GNqM7IesIzzCh8p8HIM7nRTRnsivlV9v","osversion":"and_13.0.0","id":"1809836324"}))
        gzip = decompress(con.recv()).decode('utf-8')
        if '"status":"Success"' in gzip:
            success += 1
            b = accounts.append(username + ':hhhh')
            print(b)
            with open('SafeUM.txt', 'a') as f:
                f.write(username + ":hhhh | TG : @Ali_joker\n")

        else:
            failed += 1
    except:
        retry += 1
# Check the expiry date again after creating each new account
    if datetime.datetime.now() > expiry_date:
        print("Script expired")
        return

start = ThreadPoolExecutor(max_workers=1000)

while True:
    start.submit(work)
    print('\n\n\n' + ' ' * 25 + 'Success : ' + str(success) + '\n\n\n' + ' ' * 25 + 'Failed : ' + str(
        failed) + '\n\n\n' + ' ' * 25 + 'ReTry : ' + str(retry))
    hh = str(failed) + str(success) + str(retry)
    if int(success) >= 5000:
        fuck()
        print("Created Accounts Successfully")
        
    
    if int(success) > int(0):
        z = "\n".join(accounts)
        
        print("CREATED ACCOUNTS>>\n", z)
        

    os.system('clear')

# encoding: utf-8
# Decode by Plya_Team-Pro tool...
# Copyright: Plya_Team
# Follow us on telegram ( @Plya_Team ) 
