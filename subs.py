import time
import paho.mqtt.client as mqtt
import matplotlib.pyplot as plt

localhost = '127.0.0.1'
port = 1883
timeout = 60
topic = "/test/podtest"

def on_connect(client, userdata, flags, rc):
    print("error = " + str(rc))
    client.subscribe(topic)

wektor_godz=[0]
wektor_wart=[0]

def on_message(client, userdata, msg):
    print("msg!")
    print(msg.payload)
    wiad = msg.payload.decode()
    data=wiad[0:10]
    godz=wiad[11:19]
    wart=float(wiad[-4:])
    wektor_godz.append(godz)
    wektor_wart.append(wart)
    '''print("typ wiad: ",type(wiad))
    print("wektor dat: ", wektor_dat)
    print("wektor wart: ", wektor_wart)
    print("typ data: ", type(data))
    print("typ wart: ", type(wart))
    print("typ wektor_dat ", type(wektor_dat))
    print("typ wektor_wart: ", type(wektor_dat))'''
    return wektor_dat
    return wektor_wart

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(localhost, port, timeout)
#client.loop_forever()
client.loop_start()
time.sleep(60)
client.loop_stop()

wektor_godz.pop(0)
wektor_wart.pop(0)
plt.plot(wektor_godz,wektor_wart,'bo')
plt.show()