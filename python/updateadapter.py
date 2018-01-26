from chatterbot.logic import LogicAdapter
import pymysql.cursors
import pymysql
from config import *
import chatterbotadaper

resp_str = ""
class UpdateAdapter(LogicAdapter):
    def can_process(self, statement):
        from chatterbot.conversation import Statement
        """
        Return true if the input statement contains
        Update.
        """
        global words
        global resp_str
        newRoomType=""

        set1 = ['yes','update','room']
        set2 = ['yes','update', 'check','in']

        if all(x in statement.text.split() for x in set1):
            words = statement.text.split()
            print("i am in update adapter")
            newRoomType = (words[-1])
            print("new room type = "+ newRoomType)
            print("current name in room update =" + chatterbotadaper.currentname)
            UpdateName= chatterbotadaper.currentname

            #try:
            with conn.cursor() as cursor:
                    newRoomType = (words[-1])
                    print("new room type = "+ newRoomType)
                    # userID = "SELECT id FROM slackbot.currentuser WHERE username = (%s)"
                    # cursor.execute(userID, (UpdateName) )
                    sql5 = "SELECT * FROM slackbot.currentuser WHERE username = (%s)"
                    cursor.execute(sql5, (UpdateName))
                    #print(" user id " + userID)
                    result4 = cursor.fetchone()[0]
                    print(type(result4))
                    print("user id " + str(result4))
                    updateRoom = "UPDATE  slackbot.bookings SET roomType = (%s) WHERE customer_id = (%s)"

                    cursor.execute(updateRoom, (newRoomType, result4))
                    newPrice = "SELECT RentPerNight FROM slackbot.roomtype WHERE Type=(%s)";
                    cursor.execute(newPrice,(newRoomType))
                    price = cursor.fetchone()

                    resp_str = (UpdateName +", your updated room price per day is `" + str(price[0]) + " USD `")
                    #"  * The rent per night is " + str(price[0]) + ".*"
                    conn.commit()
            #except:
                #print("SQL error !")
            return True
        if all(x in statement.text.split() for x in set2):
            words = statement.text.split()
            print("i am in update adapter")
            newRoomType = (words[-1])
            print("new room type = "+ newRoomType)
            print("current name in ckeckIn update =" + chatterbotadaper.currentname)
            UpdateName= chatterbotadaper.currentname
            try:
                with conn.cursor() as cursor:
                    newCheckIn = (words[-1])
                    print("new room type = "+ newCheckIn)
                    #print("current name in update =" + currentname)
                    userID = "SELECT id FROM slackbot.currentuser WHERE username = (%s)"
                    cursor.execute(userID, (UpdateName))
                    result4 = cursor.fetchone()[0]
                    updateCheckIn = "UPDATE  slackbot.bookings SET check_in = (%s) WHERE customer_id = (%s)"
                    cursor.execute(updateCheckIn, (newCheckIn, result4) )
                    resp_str = (UpdateName +", your check-in date has been modified. ")
                    conn.commit()
            except:
                print("SQL error !")
            return True
        else:
            return False


    def process(self, statement):
        global resp_str
        from chatterbot.conversation import Statement

        response_statement = Statement("Update completed ! \n" + resp_str )

        response_statement.confidence = 1
        print(response_statement.confidence)

        return response_statement
