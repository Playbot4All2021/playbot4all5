import RPi.GPIO as GPIO
import time
from gpiozero import LED

GPIO.setmode(GPIO.BCM)
'''
led = LED(19)
led.on()
time.sleep(100)
led.off()

'''
pin = 19

GPIO.setup(pin, GPIO.OUT)

print("led on")
GPIO.output(pin, True)
time.sleep(4)

print("led off")
GPIO.output(pin, 0)
time.sleep(2)

GPIO.cleanup()