import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(18)
    if input_state == False:
        print('Button A Pressed')
        time.sleep(0.2)
    input_state = GPIO.input(23)
    if input_state == False:
        print('Button B Pressed')
        time.sleep(0.2)
    input_state = GPIO.input(21)
    if input_state == False:
        print('Button C Pressed')
        time.sleep(0.2)
    input_state = GPIO.input(20)
    if input_state == False:
        print('Button D Pressed')
        time.sleep(0.2)
