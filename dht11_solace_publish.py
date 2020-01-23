import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import RPi.GPIO as GPIO
import dht11
import time
import json

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#GPIO.cleanup()

# read data using Pin GPIO21
instance = dht11.DHT11(pin=14)

#Connection parms for Solace Event Broker

solace_url = "mr1u6o37qngitn.messaging.solace.cloud"
solace_port = 1883
solace_user = "solace-cloud-client"
solace_passwd =  "2g71evn41v1va1jioggvch69je"
solace_clientid = "raspberry_pi"
solace_topic_temp = "devices/temperature/events"
solace_topic_humidity = "devices/humidity/events"
payload = "Hello from Raspberry Pi"

def connect_callback(client, userdata, flags, rc):
   if (rc==0):
      print("connected ok")
   else:
      print("connect failed")

client = mqtt.Client(solace_clientid)
client.on_connect=connect_callback
client.username_pw_set(username=solace_user,password=solace_passwd)

print ("Connecting to solace {}:{} as {}". format(solace_url, solace_port, solace_user))
client.connect(solace_url, port=solace_port)
client.loop_start()



while True:
    result = instance.read()
    if result.is_valid():
        print("Temp: %d C" % result.temperature +' '+"Humid: %d %%" % result.humidity)
        payload = 'Temp: ' + str(result.temperature) + '  ' + 'Humid: ' + str(result.humidity)
        temp_payload = result.temperature
        hum_payload = result.humidity
        print("Publishing a message to Solace")
        temp_payload = {"timestamp": int(time.time()), "device": "Temperature", "Temperature": temp_payload}
        temp_payload =  json.dumps(temp_payload,indent=4)
        hum_payload = {"timestamp": int(time.time()), "device": "Humidity", "Humidity": hum_payload}
        hum_payload = json.dumps(hum_payload, indent=4)

        client.publish(solace_topic_temp, temp_payload)
        client.publish(solace_topic_humidity,hum_payload)
    time.sleep(1)