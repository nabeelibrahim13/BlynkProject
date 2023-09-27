import network
def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        print(sta_if.scan())
        sta_if.connect("HUAWEI-UtK2", "FjFyt2w3")
        sta_if.connect("IoT_Device",'Thejudgementday@')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

do_connect()