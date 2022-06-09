from kafka import KafkaProducer, KafkaConsumer
import csv
from json import loads

consumer = KafkaConsumer('tweets', bootstrap_servers='kafka-server:9092', api_version=(2, 0, 2),
                         value_deserializer=lambda x: loads(x.decode('utf-8')))


def write_to_file(filename, fields):
    with open(filename, 'w+') as f:
        writer = csv.writer(f)
        writer.writerow(['author_id', 'created_at', 'text'])
        for field in fields:
            writer.writerow(field)


date = None
filename = None
fields = []
for msg in consumer:
    if msg.value['created_at'] == "end":
        break  # remove these two lines in order for the consumer to run even after all the tweets have been read
    if msg.value['created_at'] != date:
        if date is not None:
            write_to_file(filename, fields)
            fields = []
        date = msg.value['created_at']
        filename = 'tweets' + date + '.csv'
    fields.append([msg.value['author_id'], msg.value['created_at'], msg.value['text']])
