import time
import requests
from kafka import KafkaProducer
from json import dumps
import json
kafka_bootstrap_servers = "localhost:9092"

meetup_com_rsvp_stream_api_url = "http://stream.meetup.com/2/rsvps"
kafka_topic_name = "meetuprsvptopic"

if __name__ == "__main__":
    print("Kafka producer started....")
    kafka_producer_obj = KafkaProducer(bootstrap_servers= kafka_bootstrap_servers, )
