# raspberry2solace README

What does this demonstrate?
This is a demonstration of Streaming IoT sensor data ingest via raspberry pi gateway into cloud. A Solace PubSub+ Event Broker is used to asynchronously stream/distribute data to multiple consumers in cloud, on-prem etc.

### Cloud Services Used
AWS, Node-Red, PubSub + Cloud on GCP

### Solace PubSub+ features used
Open API support, Multiple protocols, Topic Filtering, Asynchronous streaming

### Other Useful Links
DHT11 Pin Configuration -  https://www.raspberrypi.org/documentation/usage/gpio/

Install Rasbian on Raspberry Pi - https://www.raspberrypi.org/documentation/installation/installing-images/

Install Node-Red on MAC/PC - https://nodered.org/docs/getting-started/local

## Contents

This repository contains
- Sensor publisher python code for Raspberry Pi to publish via MQTT to Solace PubSub+ Event Broker
- Virtual publisher python code for Raspberry Pi to publish via MQTT to Solace PubSub+ Event Broker
- Simple screen printer for Raspberry Pi to print sensor output to screen
- Node Red subscriber code to subscribe to Solace Pubsub+ Event Broker and dislay real time sensor graphs on UI
- Simpl python subscriber code to subscribe to Solace Pubsub+ Event Broker


## Checking out

To check out the project, clone this GitHub repository:

```
git clone https://github.com/solacese/raspberrypi2solace
cd raspberrypi2solace
```

## Running the Demo

Install Raspbian
https://www.raspberrypi.org/documentation/installation/installing-images/

Install python 3.7, pip3

```
sudo apt install python3-pip
```

Dependencies

```
pip3 install paho-mqtt

pip3 install Adafruit_DHT
```

Software installation/Configuration

On your Mac/PC
•	Clone/Download git repository - https://github.com/SolaceLabs/makeuoft-hackathon.git

•	Ssh into your raspberry pi

On your Raspberry Pi
•	From makeuoft-hackathon-master/raspberrypi2solace/publish on local machine

•	Copy simpletest.py, dht11.py, raspi_solace_publish_json.py and virtual_solace_publish_json.py 

o	Into any directory in raspberry pi 

On your Mac/PC 
1.	Install Node-Red - https://nodered.org/docs/getting-started/local
2.	Run node-red on terminal/command prompt
3.	Go to http://localhost:1880 to verify installation
4.	Install Dashboard Nodes - https://flows.nodered.org/node/node-red-dashboard
5.	From the folder - makeuoft-hackathon-master/raspberrypi2solace/subscribe
6.	Copy SCADA_subscribe.json to any folder on local machine
7.	Import the json into Node-Red editor from Menu-Import
8.	Follow the following instructions for config
9.	Open node “Temperature Events via Solace” Click edit


## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

See the list of [contributors](https://github.com/solacese/<github-repo>/graphs/contributors) who participated in this project.

## License

This project is licensed under the Apache License, Version 2.0. - See the [LICENSE](LICENSE) file for details.

## Resources

For more information try these resources:

- The Solace Developer Portal website at: http://dev.solace.com
- Get a better understanding of [Solace technology](http://dev.solace.com/tech/).
- Check out the [Solace blog](http://dev.solace.com/blog/) for other interesting discussions around Solace technology
- Ask the [Solace community.](http://dev.solace.com/community/)
