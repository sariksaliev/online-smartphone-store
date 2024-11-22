# Подключение к RabbitMQ
from aio_pika import connect_robust

# Конфигурация RabbitMQ (можно вынести в .env)
RABBITMQ_URL = "amqp://guest:guest@localhost/"


# Функция для подключения к RabbitMQ
async def get_rabbit_connection():
    try:
        connection = await connect_robust(RABBITMQ_URL)
        return connection
    except Exception as e:
        print(f"Ошибка подключения к RabbitMQ: {e}")
        raise
