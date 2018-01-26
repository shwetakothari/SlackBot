
from chatterbot.logic import LogicAdapter
import pymysql.cursors
import pymysql
from config import *
from roomadapter import *
from chatterbotadaper import * 
import roomadapter
import chatterbotadaper


class CheckInAdapter(LogicAdapter):
    def can_process(self, statement):
        """
        Return true if the input statement contains
        Check In.
        """
        global words
        words = statement.text.split()
        set111 = ['check', 'in', 'date']

        if all(x in statement.text.split() for x in set111):
            words = statement.text.split()
            return True
        else:
            return False

    def process(self, statement):
        from chatterbot.conversation import Statement
        print("i am in check in adapter process part ")
        print(roomadapter.typeroom)
        
        with conn.cursor() as cursor:
                userdate = words[-1]
                sql = "SELECT COUNT(*) FROM `slackbot`.`roomnumber` WHERE `roomtype` = %s"
                cursor.execute(sql,roomadapter.typeroom)
                result = cursor.fetchone()[0]
                sql2 = "SELECT COUNT(*) FROM `slackbot`.`bookings` WHERE `roomType` = '%s' AND `check_in` = '%s'" % (roomadapter.typeroom, words[-1])
                cursor.execute(sql2)
                result2 = cursor.fetchone()[0]
                if result != result2:
                   print("moke")
                   
                   sql3="SELECT `roomnumber` FROM `slackbot`.`roomnumber` WHERE `roomtype` = '%s' AND `roomnumber` NOT IN (SELECT `roomnumber` FROM `slackbot`.`bookings` WHERE `roomType` = '%s' AND `check_in` = '%s')" % (roomadapter.typeroom, roomadapter.typeroom, words[-1])
                   cursor.execute(sql3)
                   result3 = cursor.fetchone()[0]
                   sql5 = "SELECT `id` from `slackbot`.`currentuser` WHERE `username` = '%s'" % (chatterbotadaper.currentname)
                   cursor.execute(sql5)
                   result4 = cursor.fetchone()[0]
                   sql6 = "SELECT `RentPerNight` from `slackbot`.`roomtype` WHERE `Type` = '%s'" % (roomadapter.typeroom)
                   cursor.execute(sql6)
                   price = cursor.fetchone()[0]
                   sql4 = "insert into `slackbot`.bookings(roomType,check_in,roomnumber,customer_id) VALUES('%s', '%s', '%d', '%d')" % \
                           (roomadapter.typeroom, words[-1] , result3 , result4)
                   cursor.execute(sql4)
                 
                   
                   response_statement = Statement("Your booking has been done.\n Your room number is `*" + ''.join(str(result3)) + "*`. \n" + "The total price is *" + ''.join(str(price)) + "*. \n" + "Looking forward to see you on *" + ''.join(userdate) + "* \n Thank You! \n Have a great time!")
                        
                else:
                    response_statement = Statement("The room is not available! \n Please try to book for other date or room type!")
                    
        conn.commit()
        response_statement.confidence = 1
        print(response_statement.confidence)
        return response_statement
