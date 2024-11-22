import pika
import json

def send_message_to_queue(queue_name, message):
    # Подключение к RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    channel = connection.channel()

    # Объявляем очередь, если она еще не создана
    channel.queue_declare(queue=queue_name, durable=True)

    # Отправляем сообщение
    channel.basic_publish(
        exchange="",
        routing_key=queue_name,
        body=json.dumps(message),
        properties=pika.BasicProperties(delivery_mode=2)  # Сохраняем сообщение в случае сбоя
    )

    print(f"Message sent to queue {queue_name}: {message}")
    connection.close()
