import RPi.GPIO as GPIO
import time

class Robot:


    def __init__(self, pin_braccia, pin_testa):
        GPIO.setmode(GPIO.BCM)
        self.pin_testa = pin_testa
        GPIO.setup(pin_braccia, GPIO.OUT)
        self.braccia= GPIO.PWM(pin_braccia, 50)#Antiorario = alto, orario = basso
        GPIO.setup(pin_testa, GPIO.OUT)
        self.testa = GPIO.PWM(pin_testa, 50)#Antiorario = basso, orario = alto

    def reset (self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin_testa, GPIO.OUT)
        self.testa = GPIO.PWM(self.pin_testa, 50)#Antiorario = basso, orario = alto


    def reazionePositiva(self):
        '''
        Alza e abbassa le braccia
        '''
        print("1")
        self.braccia.start(5)
        time.sleep(0.5)

        print("2")
        self.braccia.ChangeDutyCycle(8)
        time.sleep(0.5)
        
        
        print("3")
        self.braccia.start(5)
        time.sleep(0.5)
        
        print("4")
        self.braccia.ChangeDutyCycle(8)
        time.sleep(0.5)
        
        self.testa.stop()


    def reazioneNegativa(self):
        '''
        Fai no con la testa
        '''
        print("1")
        self.testa.start(2.5)
        time.sleep(0.5)

        print("2")
        self.testa.ChangeDutyCycle(10)
        time.sleep(0.5)
        
        
        print("3")
        self.testa.start(2.5)
        time.sleep(0.5)
        
        print("4")
        self.testa.ChangeDutyCycle(10)
        time.sleep(0.5)
        
        self.testa.stop()

