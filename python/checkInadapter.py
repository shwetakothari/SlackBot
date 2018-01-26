
from chatterbot.logic import LogicAdapter
import pymysql.cursors
import pymysql
from config import *
from roomadapter import *
from chatterbotadaper import * 
import roomadapter
import chatterbotadaper
import datetime


class CheckInAdapter(LogicAdapter):
    def can_process(self, statement):
        """
        Return true if the input statement contains
        Check In.
        """
        global words
        words = statement.text.split()

        # User should write in this format= Check In : mm/dd/yyyy
        set111 = ['check', 'in', 'date']

        if all(x in statement.text.split() for x in set111):
            words = statement.text.split()
            print("i am in check in adapter true part ")
            return True
        else:
            print("i am in check in adapter false part ")
            return False

    def process(self, statement):
        from chatterbot.conversation import Statement
        print("i am in check in adapter process part ")
        print(roomadapter.typeroom)
        
        with conn.cursor() as cursor:
                #update bookings table with check in date at id 01
                #sql = "SELECT  COUNT(*) FROM `slackbot`.`bookings` WHERE `roomType`= %s"
                #cursor.execute(sql, 'suite')
                #result=cursor.fetchone()
                #print(result)
                #sql1 = "SELECT `NoOfRooms` FROM `slackbot`.`roomtype` WHERE `Type`=%s"
                #cursor.execute(sql1,'suite')
                #result1=cursor.fetchone()
                ##print(result1)
                #if result1 > result:
                #   available = 13
                userdate = words[-1]
                CurrentDate = "12/06/2017"
                CurrentDate = datetime.datetime.strptime(CurrentDate, "%m/%d/%Y")
                print(CurrentDate)

                ExpectedDate = words[-1]
                ExpectedDate = datetime.datetime.strptime(ExpectedDate, "%m/%d/%Y")
                print(ExpectedDate)

                if ExpectedDate > CurrentDate:
                    print("Date seems fine")
                else:
                    print("Date is in past")
                sql = "SELECT COUNT(*) FROM `slackbot`.`roomnumber` WHERE `roomtype` = %s"
                cursor.execute(sql,roomadapter.typeroom)
                result = cursor.fetchone()[0]
                #sql2 = "SELECT COUNT(*) FROM `slackbot`.`bookings` WHERE `roomtype`=%s AND `check_in`= userdate"
                sql2 = "SELECT COUNT(*) FROM `slackbot`.`bookings` WHERE `roomType` = '%s' AND `check_in` = '%s'" % (roomadapter.typeroom, words[-1])
                cursor.execute(sql2)
                result2 = cursor.fetchone()[0]
                if ExpectedDate < CurrentDate:
                    #print("Please enter another check-in Date. Your Previous entry in Invalid!")
                    response_statement = Statement("Please enter another check-in Date. Your Previous entry in Invalid!")
                elif result != result2:
                   print("moke")
                   #sql3 = "SELECT `roomnumber` FROM `slackbot`.`bookings` WHERE `roomType` = '%s' AND `check_in` = '%s'" % (roomadapter.typeroom, words[-1])
                   #cursor.execute(sql3)
                   #result3 = cursor.fetchall()
                   #print type(result3)
                   #print result3[1]
                   #format_strings = ','.join(['%s'] * len(list_of_ids))
                   #cursor.execute("DELETE FROM foo.bar WHERE baz IN (%s)" % format_strings,
                   #tuple(list_of_ids))
                   sql3="SELECT `roomnumber` FROM `slackbot`.`roomnumber` WHERE `roomnumber` NOT IN (SELECT `roomnumber` FROM `slackbot`.`bookings` WHERE `roomType` = '%s' AND `check_in` = '%s')" % (roomadapter.typeroom, words[-1])
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
                   #sql7 = "
                   
                   response_statement = Statement("Your booking has been done.Your room number is -" + ''.join(str(result3)) + ". \n" + "The total price is" + ''.join(str(price)) + ". \n" + "Looking forward to see you on" + ''.join(userdate))
                    #Statement("Please refer to the details of condo room-" + ". \n" + ''.join(Description)
                                 #+ ". \n " + "The price per night is" + ". \n " + ''.join(str(price)) + " :smile: " + BookQ)            
                else:
                    response_statement = Statement("The room is not available")
                    
        conn.commit()
                #if result > 0:
                  #sql1 = "SELECT `roomnumber` FROM `slackbot`.`roomnumber` WHERE `roomtype`=%s AND `isavailable`='Y'"
                  #cursor.execute(sql1,'suite')
                  #roomnumber = cursor.fetchone()[0]
                   #print(type(words[-1]))
                #print(type(roomnumber))
                  
                  #print(words[-1])
                  #sql2 = "insert into bookings(roomType,check_in,roomnumber,customer_id) VALUES('%s', '%s', '%d', '%d')" % \
                           #('suite', words[-1] , int(roomnumber) ,49)
                  #cursor.execute(sql2)
                  #sql3 = "UPDATE  `slackbot`.`roomnumber` SET `isavailable` = 'N' WHERE `roomnumber`='%d'"
                  #cursor.execute(sql3,roomnumber)
                  
                  
                  
                  
                
                
        #conn.commit()
        

        #response_statement = Statement("Your booking has been done  \n")#+
        #                   ''.join(str(roomnumber)))
        response_statement.confidence = 1
        print(response_statement.confidence)
        return response_statement
