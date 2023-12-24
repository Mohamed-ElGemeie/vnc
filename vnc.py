import BlynkLib
import RPi.GPIO as GPIO
from BlynkTimer import BlynkTimer
from time import sleep
import time

BLYNK_TEMPLATE_ID =  "TMPL2pDOJJph8"
BLYNK_TEMPLATE_NAME =  "New Template"
BLYNK_AUTH_TOKEN =  "iqncuc3ILPdRvwPFLDs7W4IZcbq2PWle"

pin1 = 2
pin2 = 3
motion = 4 
light = 14
buzzer = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
GPIO.setup(motion, GPIO.IN)
GPIO.setup(light, GPIO.IN)
GPIO.setup(buzzer, GPIO.OUT)


# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH_TOKEN)


def measure_light_intensity():
    light_value = GPIO.input(light)
    blynk.virtual_write(1, light_value) 
    print("Light Value:", light_value)
    return light_value

def measure_motion_intensity():
    motion_value = GPIO.input(motion)
    blynk.virtual_write(0, motion_value) 
    print("Motion Value:", motion_value)
    return motion_value


#function to sync the data from virtual pins
@blynk.on("connected")
def blynk_connected():
    print("Raspberry Pi Connected to New Blynk") 

start = time.time()

while True:
    blynk.run()
    safe = True
    if(start - time.time()>2.5):
        start=time.time()
        light_value = measure_light_intensity()
        motion_value  = measure_motion_intensity()
        if (light_value > 500 or motion_value == GPIO.HIGH):
            safe = False
        else:
            safe=True
    if(not safe):
        sleep(0.2)
        GPIO.output(pin1, GPIO.HIGH)    
        GPIO.output(pin2, GPIO.HIGH)
        GPIO.output(buzzer, GPIO.HIGH)
        sleep(0.2)
        GPIO.output(pin1, GPIO.LOW)    
        GPIO.output(pin2, GPIO.LOW)
        GPIO.output(buzzer, GPIO.LOW)

    else:
        GPIO.output(pin1, GPIO.LOW)    
        GPIO.output(pin2, GPIO.LOW)
        GPIO.output(buzzer, GPIO.LOW)


    
