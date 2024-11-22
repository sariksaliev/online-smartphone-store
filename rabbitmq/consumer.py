import pika
import json

def process_order(ch, method, properties, body):
    order = json.loads(body)
    print(f"Received order: {order}")
    # Здесь вы можете добавить логику обработки, например:
    # - Сохранить заказ в базу данных
    # - Отправить уведомление на email или SMS
    ch.basic_ack(delivery_tag=method.delivery_tag)

def consume_from_queue(queue_name):
    # Подключение к RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    channel = connection.channel()

    # Убеждаемся, что очередь существует
    channel.queue_declare(queue=queue_name, durable=True)

    # Устанавливаем обработчик сообщений
    channel.basic_consume(queue=queue_name, on_message_callback=process_order)

    print(f"Waiting for messages in queue: {queue_name}")
    channel.start_consuming()
