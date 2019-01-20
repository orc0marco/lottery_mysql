# -*-coding:utf-8-*-
# @Author  : marco
# @Time    : 2019-01-09 15:41
import csv
import pymysql


# 打开数据库连接
db = pymysql.connect("wwt.cggll8by8tsn.ap-northeast-1.rds.amazonaws.com", "wwt", "wwt110110", "lottery_activity")
cursor = db.cursor()

csv_reader = csv.reader(open("test.csv"))
for row in csv_reader:
    cursor.execute("select id from user where username = %s", row[0])
    results = cursor.fetchall()
    print(results)





