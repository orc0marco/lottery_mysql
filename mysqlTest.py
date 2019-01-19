# -*-coding:utf-8-*-
# @Author  : marco
# @Time    : 2019-01-09 15:41
import csv
import json

import pymysql
import requests


# 打开数据库连接
db = pymysql.connect("server.ip", "root", "123456", "lottery_activity")
cursor = db.cursor()

for num in range(1, 1672):
   cursor.execute("select username, countryCode, password, id  from lt_activity_user limit " + str(num * 20) + "," + str(20))
   results = cursor.fetchall()
   for row in results:
      payload = {'user': json.dumps({'username': row[0], 'countryCode': row[1], 'password': row[2]})}
      print(requests.post("http://ec2-52-198-243-77.ap-northeast-1.compute.amazonaws.com:9094/user/add", data=payload), row[3])




