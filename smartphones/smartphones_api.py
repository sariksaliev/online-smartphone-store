from fastapi import APIRouter
from database.smartphoneservice import (
    get_all_smartphones,
    add_new_smartphone,
    get_smartphone_by_id,
    update_smartphone_price,
    delete_smartphone
)

smartphone_router = APIRouter(prefix='/smartphones', tags=['Для работы со смартфонами'])


# Получение списка всех смартфонов
@smartphone_router.get('/')
async def get_all():
    all_smartphones = get_all_smartphones()
    if all_smartphones:
        return {'smartphones': all_smartphones}
    else:
        return {'message': 'Ошибка при получении списка всех смартфонов'}


# Добавление нового смартфона
@smartphone_router.post('/add')
async def add_new(brand: str, model: str, description: str, price: float):
    new_smartphone = add_new_smartphone(brand=brand, model=model, description=description, price=price)
    if new_smartphone:
        return {'message': 'Смартфон добавлен'}
    else:
        return {'message': 'Ошибка при добавлении смартфона'}


# Получение информации о конкретном смартфоне
@smartphone_router.get('/get')
async def get_by_id(smartphone_id: int):
    smartphone = get_smartphone_by_id(smartphone_id=smartphone_id)
    if smartphone:
        return {'smartphone': smartphone}
    else:
        return {'message': 'Ошибка при получении информации о смартфоне'}


# Обновление информации о смартфоне
@smartphone_router.put('/update')
async def update_price(smartphone_id: int, new_price: float):
    updated = update_smartphone_price(smartphone_id=smartphone_id, new_price=new_price)
    if updated:
        return {'message': 'Цена смартфона обновлена'}
    else:
        return {'message': 'Ошибка при обновлении цены смартфона'}


# Удаление смартфона
@smartphone_router.delete('/delete')
async def delete(smartphone_id: int):
    deleted = delete_smartphone(smartphone_id=smartphone_id)
    if deleted:
        return {'message': 'Смартфон удалён'}
    else:
        return {'message': 'Ошибка при удалении смартфона'}
