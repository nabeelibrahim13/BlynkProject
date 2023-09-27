import BlynkLib
import network
from machine import Pin
import dht


led1=Pin(2,Pin.OUT)


BLYNK_AUTH = 'TaRC7gFhnUOew9xF7cYaKaiX2TIaapOm'


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
    
def function1():
    # Logic for function 1
    blynk.virtual_write(1, 'Function 1 executed')
    print("FUNCTION 1 Executed")

def function2():
    # Logic for function 2
    blynk.virtual_write(1, 'Function 2 executed')
    print("FUNCTION 2 Executed")
def function3():
    # Logic for function 3
    blynk.virtual_write(1, 'Function 3 executed')
    print("FUNCTION 3 Executed")    

@blynk.on('V1')
def terminal_handler(value):
    # Check the received command from the terminal
    if value[0] == 'function1':
        function1()
    elif value[0] == 'function2':
        function2()
    elif value[0] == 'function3':
        function3()
    else:
        blynk.virtual_write(1, 'Custom')
        print(1, "You wrote: " + value[0])
        #blynk.virtual_write(1, "You wrote: " + value[0])
        #blynk.virtual_write(0, 'Invalid function name')



@blynk.on("V0")
def v3_write_handler(value):
    print(value)
    if int(value[0])==1:
        led1.on()
    else:
        led1.off()
        



#@blynk.on("V1")
#def terminal_write_handler(value):
#    print('V1: {}'.format(value))
#    blynk.virtual_write(0, "You wrote: " + value[0])

# Run blynk in the main thread:

while True:
    blynk.run()