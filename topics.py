import confluent_kafka.admin, pprint
def startTopcis():
    conf        = {'bootstrap.servers': 'localhost:9092'}
    kafka_admin = confluent_kafka.admin.AdminClient(conf)
    new_topic   = confluent_kafka.admin.NewTopic('topic100', 1, 1)
    new_topic2   = confluent_kafka.admin.NewTopic('topic200', 1, 1)


    kafka_admin.create_topics([new_topic,new_topic2]) # CREATE (a list(), so you can create multiple).