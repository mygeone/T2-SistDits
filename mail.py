import smtplib, ssl
from flask import Flask, request
from flask import jsonify
from kafka import producer, KafkaConsumer
import uuid
import ast

port = 465  # For SSL
password = 'wKF6hW!322628'

context = ssl.create_default_context()
def sendEmail(message):
    sender_email = "reportfromsistdist@gmail.com"
    receiver_email = "myge.one@gmail.com"
    message = """
    Subject: Hi there

    This message is sent from Python."""
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("reportfromsistdist@gmail.com", password)
        server.sendmail(sender_email, receiver_email, message)


consumer = KafkaConsumer('topic2', bootstrap_servers=['localhost:9092'],
                         auto_offset_reset='earliest', enable_auto_commit=True,
                         auto_commit_interval_ms=1000, group_id=str(uuid.uuid4()),
                         request_timeout_ms=10001,
                         consumer_timeout_ms=1000)
                        
for msg in consumer:
    message = msg.value.decode('utf-8')
    message = ast.literal_eval(message)
    print(message)
    sendEmail(message)


# Create a secure SSL context
