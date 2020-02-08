# raspberry2solace README

What does this demonstrate?
This is a demonstration of ingesting streaming IoT sensor data via raspberry pi gateway into cloud. A Solace PubSub+ Event Broker is used to asynchronously distribute data to multiple consumers in cloud, on-prem etc.

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

Install python 3.7
Install pip

```
sudo apt install python3-pip
```

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
