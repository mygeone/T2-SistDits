import smtplib, ssl
import ast
import uuid
from kafka import producer, KafkaConsumer



port = 465  # For SSL
password = 'wKF6hW!322628'

context = ssl.create_default_context()

#Envio de email con data consumida desde topic dailySummary
def sendEmail3(data):
    data = []
    sender_email = "reportfromsistdist@gmail.com"

    consumer = KafkaConsumer('dailySummary', bootstrap_servers=['localhost:9092'],
                         auto_offset_reset='earliest', enable_auto_commit=True,
                         auto_commit_interval_ms=1000, group_id=str(uuid.uuid4()),
                         request_timeout_ms=10001,
                         consumer_timeout_ms=1000)

    for msg in consumer:
        consumer.commit()
        report = ast.literal_eval(msg.value.decode('utf-8'))
    consumer.close()

    for vendor in report:
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:

            body = """
            Estimado Vendedor, \n
            el dia de ayer realizaste un total de %s ventas en en el carrito numero %s \n
            Que tengas un mal dia, saludos!""" % (report[vendor]['totalVentas'], vendor)

            server.login("reportfromsistdist@gmail.com", password)
            server.sendmail(sender_email, report[vendor]['email'], body)
            

