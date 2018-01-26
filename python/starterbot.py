import os
import time
from slackclient import SlackClient
from chatterbottrainer import chatterbottrainer
#from chatterbot import chatterbot
from config import *



# starterbot's ID as an environment variable
#BOT_ID = os.environ.get("U7YHF269H")

# constants
AT_BOT = "<@" + 'U82R14VBP' + ">"

# instantiate Slack & Twilio clients
slack_client = SlackClient('xoxb-274851165397-eeJw1dxm6LGteUaSJxanIe4u')
#State can be Greetings, Name, Book, RoomType, Days, Price, Confirm
State = "Greetings"
User = "None"


slackbot = chatterbottrainer()



def handle_command(command, channel):
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """
    response = "Not sure what you mean. Please try again"
    print(command)
    response = slackbot.getResponse(command)

    slack_client.api_call("chat.postMessage", channel=channel,
                          text=str(response), as_user=True)


def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                return output['text'].split(AT_BOT)[1].strip().lower(), \
                       output['channel']
    return None, None


if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose

    if slack_client.rtm_connect():
        print("StarterBot connected and running!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")

    conn.close()
