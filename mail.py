import smtplib, ssl
import ast



port = 465  # For SSL
password = 'wKF6hW!322628'

context = ssl.create_default_context()

def sendEmail2(data):
    sender_email = "reportfromsistdist@gmail.com"
    for vendor in data:
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            
            server.login("reportfromsistdist@gmail.com", password)

            body = """
            Estimado Vendedor, \n
            el dia de ayer realizaste un total de %s ventas en en el carrito numero %s \n
            Que tengas un mal dia, saludos!""" % (data[vendor]['totalVentas'], vendor)

            server.sendmail(sender_email, data[vendor]['email'], body)

