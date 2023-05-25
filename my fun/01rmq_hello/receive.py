import pika
import sys
import os


def main():
    # connection = pika.BlockingConnection(pika.ConnectionParameters(host='http://192.168.0.120'))
    credentials  = pika.PlainCredentials('admin','123456')
    
    #todo 第三个参数是 virtualHost 默认是 / 
    connection = pika.BlockingConnection(
        pika.ConnectionParameters('192.168.0.101+',
                                  5672,
                                  '/',
                                  credentials))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    channel.basic_consume(
        queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)