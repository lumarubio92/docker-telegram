
import time
import schedule
import requests

def telegram_bot_sendtext(bot_message):
    bot_token = ''
    bot_chatID =''
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
   # response = requests.get(send_text)
   # return response.json()


def report():
    my_message=input(" Escribe un mensaje: ")
    telegram_bot_sendtext(my_message)

schedule.every(1).seconds.do(report)


while True:
    schedule.run_pending()
    time.sleep(1)
    

