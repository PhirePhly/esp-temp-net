#!/usr/bin/env python

import paho.mqtt.client as mqtt

# User variables
data_topic = "home/tempdata"
mqtt_srvr = ""
mqtt_srvr_port = 1883


# Re-Subscribe to topics
def mqtt_on_connect(client, userdata, rc):
	client.subscribe(data_topic)

# Handle incoming MQTT messages
def mqtt_on_message(client, userdata, msg):

mqtt_client = mqtt.Client()
mqtt_client.on_connect = mqtt_on_connet
mqtt_client.on_message = mqtt_on_message

client.connect(mqtt_srvr, mqtt_srvr_port, 60)

client.loop_forever()

