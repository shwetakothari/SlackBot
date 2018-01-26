from chatterbot.logic import LogicAdapter
import pymysql.cursors
import pymysql
from config import *
import chatterbotadaper


class CancelAdapter(LogicAdapter):
    def can_process(self, statement):
        from chatterbot.conversation import Statement
        """
        Return true if the input statement contains
        Cancel.
        """
        global words

        set1 = ['yes','cancel']
        #set2 = ['yes' , 'delete']

        if all(x in statement.text.split() for x in set1):
            words = statement.text.split()
            print("i am in cancel adapter")
            print("current name in cancel =" + chatterbotadaper.currentname)
            CancelName= chatterbotadaper.currentname
            try:
                with conn.cursor() as cursor:
                    userID = "SELECT id FROM slackbot.currentuser WHERE username = (%s)"
                    cursor.execute(userID, (CancelName) )
                    result4 = cursor.fetchone()[0]

                    cancel = "DELETE FROM slackbot.bookings WHERE customer_id = (%s)"
                    cursor.execute(cancel, (result4) )
                    conn.commit()
            except:
                print("SQL error !")
            return True
        else:
            return False


    def process(self, statement):
        from chatterbot.conversation import Statement
        response_statement = Statement("Your booking has been cancelled !  ")
        response_statement.confidence = 1
        print(response_statement.confidence)
        return response_statement
