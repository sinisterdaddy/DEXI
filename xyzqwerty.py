import telepot
import time
import serial
ser = serial.Serial('COM3', 9600)

def xyzqwerty(msg):
    userName = msg['from']['first_name']
    
    content_type , chat_type, chat_id = telepot.glance(msg)
    
    if(content_type == 'text'):
        command = msg['text']
        print('got command : %s' % command)
        
        if 'hello' in command:
            bot.sendMessage(chat_id,"hello this is telebot for JArvis")
        
        if 'help' in command:
            bot.sendMessage(chat_id, 'hello %s How can i help you?' % userName)
        if 'all on' in command:
            ser.write(b'A')
            
        if 'all of' in command:
            ser.write(b'a')
        
        if 'bulb of' in command:
            ser.write(b'Q')

        if 'bulb on' in command:
            ser.write(b'W')

        if 'light of' in command:
            ser.write(b'E')

        if 'light on' in command:
            ser.write(b'R')

        if 'fan on' in command:
            ser.write(b'Y')

        if 'fan of' in command:
            ser.write(b'T')

        if 'Led on' or 'LED on' or 'L E D on' in command:
            ser.write(b'I')

        if 'Led of' or 'LED of' or 'L E D of' in command:
            ser.write(b'U')

bot = telepot.Bot('5962348748:AAEMGEsKjhv-a2uiuzSh_P7zSOQ14iZNVEg')

bot.message_loop(xyzqwerty)

while 1:
    time.sleep(20)