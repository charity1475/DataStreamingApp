import time
import requests
from kafka import KafkaProducer
from json import dump, dumps
import json
kafka_bootstrap_servers = "localhost:9092"

meetup_com_rsvp_stream_api_url = "http://stream.meetup.com/2/rsvps"
kafka_topic_name = "meetuprsvptopic"

if __name__ == "__main__":
    print("Kafka producer started....")
    kafka_producer_obj = KafkaProducer(bootstrap_servers= kafka_bootstrap_servers, value_serializer= lambda x: dumps(x).encode('utf-8'))
    print('This is the beginning of the while loop')
    while True:
        try:
            stream_api_response = requests.get(meetup_com_rsvp_stream_api_url, stream=True)
            if stream_api_response.status_code == 200:
                for api_response_message in stream_api_response.iter_lines:
                    print('message received...')
                    

