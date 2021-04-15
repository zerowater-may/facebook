# -*- coding: UTF-8 -*-
import string 
import random 
from fbchat import Client
from fbchat.models import *
import time
from random import randint
import datetime

def random_str():
    _LENGTH = 10 #10자리 
    # 대문자 
    string_pool = string.ascii_letters 
    # 대소문자 
    result = "" 
    # 결과 값 
    for _ in range(_LENGTH): 
        result += random.choice(string_pool) 
    return result

def convert_seconds_to_kor_time(in_seconds):
    """초를 입력받아 읽기쉬운 한국 시간으로 변환"""
    t1   = datetime.timedelta(seconds=in_seconds)
    days = t1.days
    _sec = t1.seconds
    (hours, minutes, seconds) = str(datetime.timedelta(seconds=_sec)).split(':')
    hours   = int(hours)
    minutes = int(minutes)
    seconds = int(seconds)
    
    result = []
    if days >= 1:
        result.append(str(days)+'일')
    if hours >= 1:
        result.append(str(hours)+'시간')
    if minutes >= 1:
        result.append(str(minutes)+'분')
    if seconds >= 1:
        result.append(str(seconds)+'초')
    return ' '.join(result)
# fbid = 'rnfqhr2@gmail.com'
# fbid = 'kys980531@naver.com'
# fbpw = 'fkaustkfl123!'

# fbid = 'cassandraatkins4512@gmail.com'
# fbpw = 'a12341234aa'

fbid = 'norahbailey1183@gmail.com'
fbpw = 'a12341234aa'



# fbid = 'kys980531@naver.com'

client = Client(fbid, fbpw)
# print("Own id: {}".format(client.uid))
# users = client.fetchAllUsers()

# print("users' IDs: {}".format([user.uid for user in users]))
# print("users' names: {}".format([user.name for user in users]))

# aa = 'Chúng tôi là Alldaybeauty - Công ty chuyên phân phối mỹ phẩm tại Hàn Quốc. Trụ sở chính được đặt tại Hàn Quốc và hiện tại chúng tôi đang bắt đầu hoạt động tại Việt Nam. Chúng tôi muốn cung cấp đa dạng các mặt hàng mỹ phẩm Hàn Quốc theo phương thức bán sỉ. Chúng tôi sẽ cung cấp thông tin sản phẩm + đơn giá qua Zalo zalo qrcode : https://bit.ly/3di3FGg'
start = time.time()
count = 1
while True:
    for id in ['100006717823527','100042537646270']:
        texts = str(count)+'|'+random_str()+'|'+convert_seconds_to_kor_time(time.time() - start)
        print(texts)
        a = client.send(Message(text=texts), thread_id=id, thread_type=ThreadType.USER)
        count += 1
        time.sleep(300)

# count = 1 
# start = time.time()
# while True:

#     for id in ['100038009107420','100013725107182','100006717823527']:
#         print(count,'|',id,convert_seconds_to_kor_time(time.time() - start))
#         client.send(Message(text="안녕하십니까 형님 ?"), thread_id=id, thread_type=ThreadType.USER)
#         time.sleep(randint(250,300))
#         count+=1
        


