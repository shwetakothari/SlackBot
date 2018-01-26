# This filr contains all the global varibles across the files. Other programs need to import this
import pymysql


conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='saloni', db='slackbot')

booking_ID = 1
customer_ID = 1
userexists = 0
