# Apache Kafka Tutorial

Project for understanding Apache Kafka fundamentals, using a food delivery system as an example.

## Architecture

1. Kafka runs as a Docker container locally, managed by Apache KRaft,
2. Python producer,
3. Python consumer (checks for new events in *Order* topic),
4. `confluent_kafka` library for Python-Kafka communication.

## Prerequisites

Install the confluent-kafka library:

```bash
pip3 install confluent-kafka
```

## Useful Commands (with usage of Kafka CLI)

### Topic Management

List topics in the Kafka cluster:

```bash
docker exec -it kafka kafka-topics --list --bootstrap-server localhost:9092
```

Describe topic metadata:

```bash
docker exec -it kafka kafka-topics --bootstrap-server localhost:9092 --describe --topic orders
```

### Consuming Events

Read all events from the beginning:

```bash
docker exec -it kafka kafka-console-consumer --bootstrap-server localhost:9092 --topic orders --from-beginning
```

## Reference

Based on [Apache Kafka Tutorial](https://www.youtube.com/watch?v=B7CwU_tNYIE).