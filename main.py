from flask import Flask, request
from flask import jsonify
from kafka import producer, KafkaConsumer
import uuid
import ast

import json
from confluent_kafka import Producer, Consumer
import socket

conf = {'bootstrap.servers': "localhost:9092",
        'client.id': socket.gethostname()}

producer = Producer(conf)


app = Flask(__name__)

#ENDPOINTS

#endpoint: /newOrder que recibe un json con los datos de la nueva orden 
@app.route('/newOrder', methods=['POST'])
def newOrder():
    data = request.data

    producer.produce('topic1', data)
    producer.flush()
    return jsonify({'status': 'OK'})

#endpoint: /getOrder que consume un json con los datos de una orden generada
@app.route('/dailySummary',methods=['GET'])
def dailySummary():
    data = []
    totalVentas = {}
    consumer = KafkaConsumer('topic1', bootstrap_servers=['localhost:9092'],
                         auto_offset_reset='earliest', enable_auto_commit=True,
                         auto_commit_interval_ms=1000, group_id=str(uuid.uuid4()),
                         request_timeout_ms=10001,
                         consumer_timeout_ms=1000)

    for msg in consumer:
        consumer.commit()
        data.append(ast.literal_eval(msg.value.decode('utf-8')))
    consumer.close()

    for report in data:
        print(report['vendor']['cart_id'])
        tempVentas = len(report['report'])
        if(report['vendor']['cart_id'] not in totalVentas):  
            totalVentas[report['vendor']['cart_id']] = {
                'email' : report['vendor']['email'],
                'totalVentas' : tempVentas
            }

    user_encode_data = json.dumps(totalVentas, indent=2).encode('utf-8')
    producer.produce('topic2', user_encode_data)

    print(totalVentas)
    return jsonify(data)
    

if __name__ == '__main__':
    app.run(debug=True)
