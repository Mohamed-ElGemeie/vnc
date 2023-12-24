import BlynkLib
import RPi.GPIO as GPIO
from BlynkTimer import BlynkTimer
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

# Led control through V0 virtual pin
@blynk.on("V0")
def v0_write_handler(value):
    if int(value[0]) is not 0:
        GPIO.output(led1, GPIO.HIGH)
        print('LED1 HIGH')
    else:
        GPIO.output(led1, GPIO.LOW)
        print('LED1 LOW')

# Led control through V0 virtual pin
@blynk.on("V1")
def v1_write_handler(value):
#    global led_switch
    if int(value[0]) is not 0:
        GPIO.output(led2, GPIO.HIGH)
        print('LED2 HIGH')
    else:
        GPIO.output(led2, GPIO.LOW)
        print('LED2 LOW')

#function to sync the data from virtual pins
@blynk.on("connected")
def blynk_connected():
    print("Raspberry Pi Connected to New Blynk") 

while True:
    blynk.run()

    