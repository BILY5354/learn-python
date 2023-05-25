import pika

# connection = pika.BlockingConnection(
#     pika.ConnectionParameters(host='192.168.0.120',
#                               port=5672,
#                               '/',
#                               credentials=credentials))
credentials  = pika.PlainCredentials('admin','123456')
connection = pika.BlockingConnection(
    pika.ConnectionParameters('192.168.0.101',
                              5672,
                              '/',
                              credentials))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body='New Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()