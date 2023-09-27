from time import sleep
from hcsr04 import HCSR04
import dht
from machine import Pin
import BlynkLib
import network
import machine
import time
from machine import Pin
import dht
import wificonnect

sensor = HCSR04(trigger_pin=27, echo_pin=26, echo_timeout_us=10000)

BLYNK_AUTH = 'TaRC7gFhnUOew9xF7cYaKaiX2TIaapOm'

wificonnect.do_connect()

wifi = network.WLAN(network.STA_IF)
wifi.active(True)


while not wifi.isconnected():
    pass

print('IP:', wifi.ifconfig()[0])

blynk = BlynkLib.Blynk(BLYNK_AUTH)

@blynk.on("connected")
def blynk_connected(ping):
    print("Connecting.............")
    print('Blynk ready. Ping:', ping, 'ms')
    print("Connected!")
    #while True:
        #distance = sensor.distance_cm()
        #print('Distance:', distance, 'cm')
        #blynk.virtual_write("20",distance)
        #sleep(1)
        
def dist():
    a = 0
    while a<10:
        distance = sensor.distance_cm()
        print('\nDistance:', distance, 'cm')
        blynk.virtual_write(1, "\nDistance is", distance)
        blynk.virtual_write(3, distance)
        blynk.virtual_write(2, distance)
        blynk.virtual_write(4, distance)
        #blynk.virtual_write("20",distance)
        sleep(1)
        a+=1


@blynk.on('V1')
def terminal_handler(value):
    if value[0] == 'f1':
        dist()
    else:
        blynk.virtual_write(1, 'Custom')
        print(1, "You wrote: " + value[0])    
    # Check the received command from the terminal
    
    #print(1, "You wrote: " + value[0])


# Run blynk in the main thread:
while True:
    blynk.run()