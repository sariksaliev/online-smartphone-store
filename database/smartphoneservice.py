from database.models import Smartphone
from database import get_db


# Получение списка всех смартфонов
def get_all_smartphones():
    try:
        db = next(get_db())
        all_smartphones = db.query(Smartphone).all()
        return all_smartphones
    except Exception as e:
        # Обработка ошибок, например, логирование и возврат сообщения об ошибке
        return f'Ошибка при получении списка смартфонов: {str(e)}'


# Добавление нового смартфона
def add_new_smartphone(brand, model, description, price):
    db = next(get_db())

    # Проверяем, существует ли уже такой смартфон
    smartphone = db.query(Smartphone).filter_by(
        brand=brand,
        model=model,
        description=description,
        price=price
    ).first()

    # Если смартфон не существует, добавляем его в базу данных
    if not smartphone:
        new_smartphone = Smartphone(brand=brand, model=model, description=description, price=price)
        db.add(new_smartphone)
        db.commit()
        return 'Смартфон успешно добавлен'
    else:
        return 'Смартфон уже существует'


# Получение объекта смартфона по идентификатору
def get_smartphone_by_id(smartphone_id):
    db = next(get_db())
    smartphone = db.query(Smartphone).filter_by(id=smartphone_id).first()
    if smartphone:
        return smartphone
    else:
        return 'Смартфон не найден'


# Обновление цены смартфона
def update_smartphone_price(smartphone_id, new_price):
    db = next(get_db())
    smartphone = db.query(Smartphone).filter_by(id=smartphone_id).first()
    if smartphone:
        smartphone.price = new_price
        db.commit()
        return 'Цена смартфона успешно обновлена'
    else:
        return 'Смартфон не найден'


# Удаление смартфона
def delete_smartphone(smartphone_id):
    db = next(get_db())
    smartphone = db.query(Smartphone).filter_by(id=smartphone_id).first()
    if smartphone:
        db.delete(smartphone)
        db.commit()
        return 'Смартфон успешно удалён'
    else:
        return 'Смартфон не найден'

