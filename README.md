kubectl get secret client1 -n kafka -o jsonpath='{.data.password}' | base64 --decode
zqpa9rMShtaeoB7FeYdsHP37QoUxj8Gi

kubectl get secret client2 -n kafka -o jsonpath='{.data.password}' | base64 --decode
yEuzmJmRP1Wbtxu97Fqxy7FJmSjbwIF7

kubectl get secret admin -n kafka -o jsonpath='{.data.password}' | base64 --decode
HQxue2IS5Wbtabd6kqaOOHWzuLCTrssV


###USE ADMIN INSIDE POD###

1️⃣ Create a proper JAAS file

Inside the pod (or locally):

cat > /tmp/kafka_client_jaas.conf <<EOF
KafkaClient {
  org.apache.kafka.common.security.scram.ScramLoginModule required
  username="admin"
  password="HQxue2IS5Wbtabd6kqaOOHWzuLCTrssV";
};
EOF


Important: wrap the config inside KafkaClient { ... };, not just ScramLoginModule. This is the standard JAAS format.

2️⃣ Export KAFKA_OPTS to point to this file
export KAFKA_OPTS="-Djava.security.auth.login.config=/tmp/kafka_client_jaas.conf"


This ensures the Kafka CLI uses the JAAS file for authentication.

Do not put sasl.jaas.config inside the CLI --command-config anymore.

3️⃣ Create a standard client.properties for other Kafka configs
cat > /tmp/client.properties <<EOF
bootstrap.servers=localhost:9094
security.protocol=SASL_PLAINTEXT
sasl.mechanism=SCRAM-SHA-512
EOF


Note: property is sasl.mechanism not sasl.mechanisms in CLI properties file.

###CHECK###

bin/kafka-console-consumer.sh   --bootstrap-server localhost:9094   --topic 'client1-topic'   --from-beginning   --consumer.config /tmp/client.properties   --max-messages 20

bin/kafka-topics.sh --bootstrap-server localhost:9094 --command-config /tmp/client.properties --list