from confluent_kafka import Producer, Consumer

def run_client(username, password, topic):
    conf = {
        'bootstrap.servers': "192.168.49.2:31207",
        'security.protocol': 'SASL_PLAINTEXT',
        'sasl.mechanisms': 'SCRAM-SHA-512',
        'sasl.username': username,
        'sasl.password': password,
        'group.id': f'{username}-group',
        'auto.offset.reset': 'earliest'
    }

    # Producer
    producer = Producer(conf)
    producer.produce(topic, key="key", value=f"Hello from {username}")
    producer.flush()
    print(f"{username} produced a message to {topic}")

    # Consumer
    consumer = Consumer(conf)
    consumer.subscribe([topic])
    msg = consumer.poll(5.0)
    if msg:
        print(f"{username} consumed: {msg.value().decode('utf-8')}")
    consumer.close()

# Run clients
run_client('client1', 'zqpa9rMShtaeoB7FeYdsHP37QoUxj8Gi', 'topic1')
run_client('client2', 'yEuzmJmRP1Wbtxu97Fqxy7FJmSjbwIF7', 'topic2')
run_client('client1', 'zqpa9rMShtaeoB7FeYdsHP37QoUxj8Gi', 'topic2')
run_client('client2', 'yEuzmJmRP1Wbtxu97Fqxy7FJmSjbwIF7', 'topic1')

