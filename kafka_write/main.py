from time import sleep
from kafka import KafkaProducer, KafkaConsumer
import csv
from json import dumps
from datetime import datetime
import sys

producer = KafkaProducer(bootstrap_servers='kafka-server:9092', api_version=(2, 0, 2),
                         value_serializer=lambda x: dumps(x).encode('utf-8'))

with open('/opt/app/twcs.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    try:
        for row in reader:
            row['created_at'] = str(datetime.now().strftime('%d_%m_%Y_%H_%M'))
            data = {'created_at': row['created_at'], 'text': row['text'], 'author_id': row['author_id']}
            result = producer.send('tweets', data)
            sleep(0.001)
        producer.send('tweets', {'created_at': 'end', 'text': 'end', 'author_id': 'end'})
        producer.flush()
    except KeyboardInterrupt:
        sys.exit(0)
