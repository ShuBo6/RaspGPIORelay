from telegram import ext
from telegram.ext import CommandHandler
import RPi.GPIO as GPIO


def hello_world(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello World!")


def gpio_init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(12, GPIO.OUT)


def led_on(update, context):
    gpio_init()
    GPIO.output(12, GPIO.HIGH)
    context.bot.send_message(chat_id=update.effective_chat.id, text="灯开开了")


def led_off(update, context):
    gpio_init()
    GPIO.output(12, GPIO.LOW)
    context.bot.send_message(chat_id=update.effective_chat.id, text="灯关上了")

def fan_on(update, context):
    gpio_init()
    GPIO.output(16, GPIO.HIGH)
    context.bot.send_message(chat_id=update.effective_chat.id, text="风扇开开了")

def fan_off(update, context):
    gpio_init()
    GPIO.output(16, GPIO.LOW)
    context.bot.send_message(chat_id=update.effective_chat.id, text="风扇关上了")


updater = ext.Updater(token='1809519881:AAG_iNzUMwvbum5hz8GFcYLxFOxSTL2LEkw',
                      request_kwargs={'proxy_url': 'http://home.shubo6.cn:17890'})
dispatcher = updater.dispatcher

helloWorld = CommandHandler('helloworld', hello_world)
ledon = CommandHandler('ledon', led_on)
fanon = CommandHandler('fanon', fan_on)
ledoff = CommandHandler('ledoff', led_off)
fanoff = CommandHandler('fanoff', fan_off)

dispatcher.add_handler(helloWorld)
dispatcher.add_handler(ledon)
dispatcher.add_handler(ledoff)
dispatcher.add_handler(fanon)
dispatcher.add_handler(fanoff)

updater.start_polling()
