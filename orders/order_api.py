from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from database import get_db
from database.orderservice import (
    creation_new_order,
    # исправлено имя функции
    get_all_orders,
    get_order_by_id,
    update_order,
    delete_order, all_orders
)

order_router = APIRouter(prefix='/order', tags=['Для работы с заказами'])


# Создание нового заказа
@order_router.post('/new-order')
async def create_order(smartphone_id: int, customer_id: int):  # исправлено на smartphone_id
    new_order = creation_new_order(smartphone_id, customer_id)  # исправлено имя параметра
    if not new_order:
        raise HTTPException(status_code=400, detail="Не удалось создать заказ")
    return {"message": new_order}


# Получить все заказы клиента
@order_router.get('/customer-orders')
async def get_customer_orders(customer_id: int, db: Session = Depends(get_db)):
    orders = all_orders(db=db, customer_id=customer_id)  # Передаем db в функцию
    if isinstance(orders, dict) and "message" in orders:
        raise HTTPException(status_code=404, detail=orders["message"])
    return orders



# Получить все заказы
@order_router.get("/all-orders")
async def fetch_all_orders():
    all_orders = get_all_orders()
    if not all_orders or isinstance(all_orders, str):
        raise HTTPException(status_code=404, detail="Нет заказов")
    return all_orders


# Получение информации о конкретном заказе
@order_router.get('/order-info')
async def fetch_order(order_id: int):
    order = get_order_by_id(order_id=order_id)
    if not order or isinstance(order, str):
        raise HTTPException(status_code=404, detail="Заказ не найден")
    return order


# Обновление заказа
@order_router.put('/update-order')
async def update_order_info(order_id: int, smartphone_id: int):  # исправлено на smartphone_id
    success = update_order(order_id, smartphone_id)  # исправлено имя параметра
    if success == 'Заказ успешно обновлён':
        return {'message': success}
    else:
        raise HTTPException(status_code=404, detail=success)


# Удаление заказа
@order_router.delete('/delete-order')
async def remove_order(order_id: int):  # изменено имя функции для консистентности
    success = delete_order(order_id)
    if success == 'Заказ успешно удалён':
        return {'message': success}
    else:
        raise HTTPException(status_code=404, detail=success)
