### Apache Kafka Tutorial ###
Project for understanding Apache Kafka fundamentals. As an example foood delivery system was developer.

### Architecture ###
1. Kafka run as a Docker container locally,
2. Python producer,
3. Python consumer (is checking constantly if there is a new event in an Order),
4. confluent_kafka - a library used for enabling Python application to communicate with Kafka, 
4. Apache KRaft - for managing Kafka cluster.

Repository created based on https://www.youtube.com/watch?v=B7CwU_tNYIE.

Apache KRaft is used for managing cluster.

Producer will be a Order service which will generate an event when food order is placed on a website.
Afterwards, that event will be consumed by a consumer.


### Prerequisites ###
confluent-kafka should be installed with help of following command:

```pip3 install confluent-kafka```

### Useful commands (with usage of Kafka CLI) ###
Listing topic present within Kafka cluster:
```docker exec -it kafka kafka-topics --list --bootstrap-server localhost:9092```

Describing metadata of topic associated within Kafka cluster:
```docker exec -it kafka kafka-topics --bootstrap-server localhost:9092 --describe --topic orders```

Listing all the events which arose from a beginning:
```docker exec -it kafka kafka-console-consumer --bootstrap-server localhost:9092 --topic orders --from-beginning```