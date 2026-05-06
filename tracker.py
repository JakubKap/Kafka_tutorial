import json

from confluent_kafka import Consumer

consumer_config = {
    'bootstrap.servers': 'localhost:9092',
    "group.id": "order-tracker", #belonging to consumer group
    "auto.offset.reset": "earliest" #tells consumer what to do it cannot find where it last left off reading messages
    # from each message it should start
}

consumer = Consumer(consumer_config)

consumer.subscribe(["orders"])
print("🟢 Consumer is running and subscribed to orders topic")

while True:
    msg = consumer.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        print(f"❗Error:",  msg.error())
        continue

    value = msg.value().decode("utf-8")
    order = json.loads(value)

    print(f"📦 Received order: {order['quantity']} x {order['item']} from {order['user']}")