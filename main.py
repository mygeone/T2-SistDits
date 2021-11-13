from flask import Flask, request
import smtplib, ssl
from flask import jsonify
from kafka import producer, KafkaConsumer
import uuid
import ast
import os
from mail import sendEmail2
import json
from confluent_kafka import Producer, Consumer
import socket
from topics import *

conf = {'bootstrap.servers': "localhost:9092",
        'client.id': socket.gethostname()}

producer = Producer(conf)


app = Flask(__name__)
startTopcis()

#ENDPOINTS

#endpoint: /newOrder que recibe un json con los datos de la nueva orden 
@app.route('/newOrder', methods=['POST'])
def newOrder():
    data = request.data

    producer.produce('newOrders', data)
    producer.flush()
    return jsonify({'status': 'OK'})

#endpoint: /getOrder que consume un json con los datos de una orden generada
@app.route('/dailySummary',methods=['GET'])
def dailySummary():
    data = []
    totalVentas = {}
    consumer = KafkaConsumer('newOrders', bootstrap_servers=['localhost:9092'],
                         auto_offset_reset='earliest', enable_auto_commit=True,
                         auto_commit_interval_ms=1000, group_id=str(uuid.uuid4()),
                         request_timeout_ms=10001,
                         consumer_timeout_ms=1000)

    for msg in consumer:
        consumer.commit()
        data.append(ast.literal_eval(msg.value.decode('utf-8')))
    consumer.close()

    for report in data:
        tempVentas = len(report['report'])
        if(report['vendor']['cart_id'] not in totalVentas):  
            totalVentas[report['vendor']['cart_id']] = {
                'email' : report['vendor']['email'],
                'totalVentas' : tempVentas
            }
        else:
            totalVentas[report['vendor']['cart_id']]['totalVentas'] += tempVentas


    user_encode_data = json.dumps(totalVentas, indent=2).encode('utf-8')
    
    #produce resumen ventas
    producer.produce('dailySummary', user_encode_data)

    #send email
    sendEmail2(totalVentas)

    return jsonify(totalVentas)
    

if __name__ == '__main__':
    app.run(debug=True)
