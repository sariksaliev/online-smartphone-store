from fastapi import APIRouter
from database.customersupport import (
    create_new_customer,
    update_customer_balance,
    delete_customer,
    get_customer_info,
    get_all_customers
)
from customer import CustomerValidator


cus_router = APIRouter(prefix='/customer', tags=['Работа с клиентами'])


# Создаем нового клиента
@cus_router.post("/")
async def create_new_customer_1(customer: CustomerValidator):
    new_customer = create_new_customer(
        name=customer.name,
        surname=customer.surname,
        phone_number=customer.phone_number,
        address=customer.address
    )
    if new_customer:
        return {"message": f"Клиент {customer.name} {customer.surname} успешно создан"}
    else:
        return {"message": "Ошибка при создании клиента"}


# Обновляем баланс клиента
@cus_router.put("/update")
async def update_customer_balance_endpoint(customer_id: int, balance: float):
    updated_customer = update_customer_balance(customer_id, balance)
    if updated_customer:
        return {"message": f"Баланс клиента с ID {customer_id} успешно обновлен"}
    else:
        return {"message": f"Клиент с ID {customer_id} не найден"}


# Удаляем клиента
@cus_router.delete("/delete")
async def delete_customer_endpoint(customer_id: int):
    deleted_customer = delete_customer(customer_id)
    if deleted_customer:
        return {"message": f"Клиент с ID {customer_id} успешно удален"}
    else:
        return {"message": f"Клиент с ID {customer_id} не найден"}


# Получаем информацию о клиенте по его ID
@cus_router.get("/get")
async def get_customer_info_endpoint(customer_id: int):
    customer = get_customer_info(customer_id)
    if customer:
        return {"customer_info": customer}
    else:
        return {"message": f"Клиент с ID {customer_id} не найден"}


# Получаем список всех клиентов
@cus_router.get("/all")
async def get_all_customers_endpoint():
    all_customers = get_all_customers()
    return {"customers": all_customers}
