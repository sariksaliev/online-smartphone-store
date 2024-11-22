from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from rabbitmq.publisher import send_message_to_queue
from orders.order_api import order_router
from database.customersupport import is_customer_valid
from database.smartphoneservice import get_all_smartphones


app = FastAPI()

# Подключаем маршруты из order_api
app.include_router(order_router)


# Модель для запроса
class OrderRequest(BaseModel):
    customer_name: str
    phone_model: str
    quantity: int


@app.post("/order")
async def create_order(order: OrderRequest):
    # Проверяем валидность клиента
    if not is_customer_valid(order.customer_name):
        raise HTTPException(status_code=400, detail="Invalid customer")

@app.get("/smartphones")
async def list_smartphones():
    phones = get_available_phones()
    return {"available_phones": phones}

    try:
        # Формируем сообщение
        message = {
            "customer_name": order.customer_name,
            "phone_model": order.phone_model,
            "quantity": order.quantity
        }
        # Отправляем сообщение в RabbitMQ
        send_message_to_queue(queue_name="orders", message=message)
        return {"status": "success", "message": "Order sent to RabbitMQ"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
