from chatterbot import ChatBot
import logging
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

'''
This is an example showing how to train a chat bot using the
ChatterBot Corpus of conversation dialog.
'''


# Enable info level logging
class chatterbottrainer:

    def __init__(self):

       print("chatterbottrainer init")

       logging.basicConfig(level=logging.DEBUG)

       self.chatbot = ChatBot(
           'Example Bot',
           trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
           input_adapter="chatterbot.input.VariableInputTypeAdapter",
           output_adapter="chatterbot.output.OutputAdapter",
           output_format="text",
           logic_adapters=[
               {
                   'import_path': 'chatterbot.logic.BestMatch'
               },
               {
                   'import_path': 'chatterbotadaper.MyLogicAdapter'
               },
               {
                   'import_path': 'roomadapter.RoomAdapter'
               },
               {
                   'import_path': 'checkInadapter.CheckInAdapter'
               },
               {
                   'import_path': 'updateadapter.UpdateAdapter'
               },
               {
                   'import_path': 'canceladapter.CancelAdapter'
               },
               {
                   'import_path': 'chatterbot.logic.LowConfidenceAdapter',
                   'threshold': 0.65,
                   'default_response': 'I am sorry, I do not understand.'
               }
           ]
       )

       #chatbot.set_trainer(ChatterBotCorpusTrainer)

       conv = open('data/test.txt','r').readlines()

       self.chatbot.set_trainer(ListTrainer)


       self.chatbot.train(conv)



    def getResponse(self,request):
       print("chatterbottrainer init "+request)

       response = self.chatbot.get_response(request)
       print(response)
       return response
