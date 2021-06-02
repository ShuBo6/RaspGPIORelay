from flask import Flask
import RPi.GPIO as GPIO


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

def gpio_init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(12, GPIO.OUT)

@app.route('/ledon')
def led_on():
    gpio_init()
    GPIO.output(12, GPIO.HIGH)
    return 'led_on'

@app.route('/ledoff')
def led_off():
    gpio_init()
    GPIO.output(12, GPIO.LOW)
    return 'led_off'

@app.route('/fanon')
def fan_on():
    gpio_init()
    GPIO.output(16,GPIO.HIGH)
    return 'fan_on'

@app.route('/fanoff')
def fan_off():
    gpio_init()
    GPIO.output(16,GPIO.LOW)
    return 'fan_off'



if __name__ == '__main__':
    app.run()
