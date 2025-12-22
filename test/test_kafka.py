from kafka import KafkaProducer, KafkaConsumer
from kafka.admin import KafkaAdminClient, NewTopic
import json
import time


def test_kafka():
    try:
        # Test connection
        admin = KafkaAdminClient(bootstrap_servers=['localhost:9092'])
        print("✅ Kafka connection successful")

        # Create test topic
        topic = NewTopic(name='test-topic', num_partitions=1, replication_factor=1)
        try:
            admin.create_topics([topic])
            print("✅ Test topic created")
        except Exception:
            print("✅ Test topic already exists")

        # Test producer
        producer = KafkaProducer(
            bootstrap_servers=['localhost:9092'],
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        producer.send('test-topic', {'message': 'Hello from Kafka 4.0!'})
        producer.flush()
        producer.close()
        print("✅ Message sent successfully")

        # Test consumer
        time.sleep(1)
        consumer = KafkaConsumer(
            'test-topic',
            bootstrap_servers=['localhost:9092'],
            value_deserializer=lambda m: json.loads(m.decode('utf-8')),
            consumer_timeout_ms=3000,
            auto_offset_reset='earliest'
        )

        for message in consumer:
            print(f"✅ Message received: {message.value}")
            break

        consumer.close()
        print("✅ All Kafka tests passed!")

    except Exception as e:
        print(f"❌ Test failed: {e}")


if __name__ == "__main__":
    test_kafka()