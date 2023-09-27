try:
    import urequests as requests
except:
    import requests

import random
import time
import network
import gc
from time import sleep
from hcsr04 import HCSR04
import dht
import BlynkLib
import machine
from machine import Pin
import wificonnect

sensor = HCSR04(trigger_pin=27, echo_pin=26, echo_timeout_us=10000)

def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('Connecting to network...')
        sta_if.active(True)
        sta_if.connect("HUAWEI-UtK2", 'FjFyt2w3')
        while not sta_if.isconnected():
            pass
    print('Network config:', sta_if.ifconfig())

do_connect()

phone_number = '923352541678'
# Your callmebot API key
api_key = '4277729'

def send_message(phone_number, api_key, message):
    # Set your host URL
    url = 'https://api.callmebot.com/whatsapp.php?phone='+phone_number+'&text='+message+'&apikey='+api_key
    try:
        # Make the request to send a WhatsApp message
        response = requests.get(url)
        if response.status_code == 200:
            print('WhatsApp message sent successfully!')
        else:
            print('Waiting for 1 second')
        response.close()
    except Exception as e:
        print('Error occurred while sending WhatsApp message:', str(e))

if __name__ == "__main__":
    while True:
        try:
            # Send a WhatsApp message
            distance = sensor.distance_cm()
            if distance>20:
                a = 'Too%20Far'
            elif distance>10:
                a = 'average'
            else:
                a = 'to%20close'
            
#             message = 'Hello%20This%20is%20testing%20message%20service%0Aby%20ESP32'+str(distance)+a
            message = f"Distance%20Value%3A%20{distance}%20{a}"
            send_message(phone_number, api_key, message)
            gc.collect()
            time.sleep(1)  # Adjust the delay as needed
        except KeyboardInterrupt:
            break

network.WLAN(network.STA_IF).disconnect()