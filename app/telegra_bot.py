
from datetime import datetime
import time
import schedule
import requests


def telegram_bot_sendtext(bot_message):
    
    bot_token = ''
    bot_chatID =''     
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()

hora="23:53"
def report():
    my_balance = hora  ## 
    my_message = "este mensaje es de un bot son las: {}".format(my_balance)  
    telegram_bot_sendtext(my_message)

def time_now():
    now = datetime.now()
    print("hora: ",now)
    return now

schedule.every().day.at(hora).do(report)

while True:
    schedule.run_pending()
    time_now()
    time.sleep(1)
