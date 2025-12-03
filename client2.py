from kafka import KafkaProducer, KafkaConsumer

BROKER = "192.168.49.2:31207"       # use your Strimzi external listener address
TOPIC = "test-topic"
USERNAME = "test-user"
PASSWORD = "S63Y4XO3MW54BIq3ASwx4LgFioDspCCi"

# ---------- PRODUCER ----------
producer = KafkaProducer(
    bootstrap_servers=[BROKER],
    security_protocol="SASL_PLAINTEXT",
    sasl_mechanism="SCRAM-SHA-512",
    sasl_plain_username=USERNAME,
    sasl_plain_password=PASSWORD,
    value_serializer=lambda v: v.encode("utf-8"),
)

producer.send(TOPIC, "hello from client1")
producer.flush()
print("Produced OK")

# ---------- CONSUMER ----------
consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=[BROKER],
    security_protocol="SASL_PLAINTEXT",
    sasl_mechanism="SCRAM-SHA-512",
    sasl_plain_username=USERNAME,
    sasl_plain_password=PASSWORD,
    auto_offset_reset="earliest",
    value_deserializer=lambda b: b.decode("utf-8"),
)

print("Waiting for messages...")
for msg in consumer:
    print("Consumed:", msg.value)
    break
