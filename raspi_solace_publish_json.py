
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time
import Adafruit_DHT
import json

payload = "Hello from Raspberry Pi"
sensor = Adafruit_DHT.DHT11
pin = 14
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
    payload = 'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity)
else:
    print('Failed to get reading. Try again!')
    
solace_url = "mr1u6o37qngitn.messaging.solace.cloud"
solace_port = 1883
solace_user = "solace-cloud-client"
solace_passwd =  "2g71evn41v1va1jioggvch69je"
solace_clientid = "raspberry_pi"
solace_topic = "test/raspi"


def parse_command_line_args():
    """Parse command line arguments."""

    parser.add_argument(
            '--device_id', required=True, help='Cloud IoT Core device id')
    parser.add_argument(
            '--num_messages',
            type=int,
            default=100,
            help='Number of messages to publish.')
    parser.add_argument('--solace', default=False, action='store_true', help='Is it connecting to solace')
    parser.add_argument('--client_username',  action='store', help='client username')
    parser.add_argument('--client_password',  action='store', help='client password')
    parser.add_argument(
            '--mqtt_bridge_port',
            default=1883,
            type=int,
            help='MQTT bridge port.')

    return parser.parse_args()

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


#print ("Publish a message to {}" .format (solace_topic))
#client.publish(solace_topic, payload)
#time.sleep(1)
#client.loop_stop()
#client.disconnect()


# Publish num_messages mesages to the MQTT bridge once per second.
for i in range(1, 5):
    client.loop_start()
    #simulated_temp = simulated_temp + temperature_trend * random.normalvariate(0.01,0.005)

    #payload = {"timestamp": int(time.time()), "device": args.device_id, args.device_id: payload}
    payload = {"timestamp": int(time.time()), "device": "temphum", "temphum": payload}

    #print('Publishing message {} of {}: <{}> \'{}\''.format(
    #        i, 2, solace_topic, payload))
    jsonpayload =  json.dumps(payload,indent=4)
    # Publish "jsonpayload" to the MQTT topic. qos=1 means at least once
    # delivery. Cloud IoT Core also supports qos=0 for at most once
    # delivery.
    client.publish(solace_topic, jsonpayload, qos=1)

    # Send events every second. State should not be updated as often
    time.sleep(1)

# End the network loop and finish.
client.loop_stop()
client.disconnect()
print('Finished.')

