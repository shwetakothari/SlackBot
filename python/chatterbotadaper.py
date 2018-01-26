
from chatterbot.logic import LogicAdapter
import pymysql.cursors
import pymysql
from config import *

userexists = 0
currentname=""
class MyLogicAdapter(LogicAdapter):
    def can_process(self, statement):
        """
        Return true if the input statement contains
        'what' and 'is' and 'temperature'.
        """
        #global userexists
        set1 = ['i', 'am']
        set2 = ['my', 'name']
        set3 = ['username','is']

        global userexists

        if all(x in statement.text.split() for x in set1):
            words = statement.text.split()
            try:
             with conn.cursor() as cursor:
                    # Create a new record
                    #print("saloni")
                    sql = "SELECT COUNT(1) FROM `slackbot`.`currentuser` WHERE `username` = %s"
                    cursor.execute(sql, (words[-1]))
                    if cursor.fetchone()[0]:
                       print("The username already exists in the database.")
                       userexists = 1
                       currentname= (words[-1])
                       print("current name in chatterbot =" + currentname)
                       #return("The username already exists, please renter another username in the format Username : Yourusername")
                    else:
					#sql = "UPDATE  `slackbot`.`currentuser` SET `username` = %s"
                      print("sanju")
                      add_employee = ("INSERT INTO `currentuser` " "(username) " "VALUES (%s)")
                      cursor.execute(add_employee, (words[-1]))
                      conn.commit()
            except:
                print("This is an sql error message!")
            return True
        elif all(x in statement.text.split() for x in set2):
            words = statement.text.split()
            try:
             with conn.cursor() as cursor:
                    # Create a new record
                    #print("saloni")
                    sql = "SELECT COUNT(1) FROM `slackbot`.`currentuser` WHERE `username` = %s"
                    cursor.execute(sql, (words[-1]))
                    if cursor.fetchone()[0]:
                       print("The username already exists in the database.")
                       userexists = 1
                       #return("The username already exists, please renter another username in the format Username : Yourusername")
                    else:
					#sql = "UPDATE  `slackbot`.`currentuser` SET `username` = %s"
                      print("sanju")
                      add_employee = ("INSERT INTO `currentuser` " "(username) " "VALUES (%s)")
                      cursor.execute(add_employee, (words[-1]))
                      conn.commit()
            except:
                print("This is an sql error message!")
            return True

        elif all(x in statement.text.split() for x in set3):
            print("kamesh")
            words = statement.text.split()
            print(words[-1])
            try:
             with conn.cursor() as cursor:
                    # Create a new record
                    #print("saloni")
                    sql = "SELECT COUNT(1) FROM `slackbot`.`currentuser` WHERE `username` = %s"
                    cursor.execute(sql, (words[-1]))
                    if cursor.fetchone()[0]:
                       print("The username already exists in the database. ")
                       userexists = 1
                       #return("The username already exists, please renter another username in the format Username : Yourusername")
                    else:
					#sql = "UPDATE  `slackbot`.`currentuser` SET `username` = %s"
                      print("sanju")
                      add_employee = ("INSERT INTO `currentuser` " "(username) " "VALUES (%s)")
                      cursor.execute(add_employee, (words[-1]))
                      conn.commit()
            except:
                print("This is an sql error message!")
            return True

        else:
         return False




    def process(self, statement):
        global userexists
        from chatterbot.conversation import Statement
        words = statement.text.split()
        global currentname
        currentname = words[-1]
        if userexists == 1:
          response_statement = Statement('There is already another user with the same username.Please enter another username in the format username is "yourusername" or if you have already done the booking with the same username enter "update" for updating the booking and "delete" for deleting the booking')
          userexists = 0
        else:
          response_statement = Statement('Welcome '+ words[-1] +'! \n Which room do you want Suite room , Deluxe room  or Condo room?')
        response_statement.confidence = 1 
        print(response_statement.confidence)
        return response_statement
