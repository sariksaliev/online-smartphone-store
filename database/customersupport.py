from database import get_db
from database.models import Customer


# Проверка клиента по номеру телефона
def is_customer_valid(phone_number: int) -> bool:
    db = next(get_db())
    customer = db.query(Customer).filter_by(phone_number=phone_number).first()
    return customer is not None


# Создаем клиента
def create_new_customer(name: str, surname: str, phone_number: int, address: str):
    try:
        db = next(get_db())

        # Проверка на существование клиента
        if is_customer_valid(phone_number):
            return {'message': 'Клиент с таким номером телефона уже существует'}

        # Если клиента нет, создаем нового
        new_customer = Customer(name=name, surname=surname, phone_number=phone_number, address=address, balance=0.0)
        db.add(new_customer)
        db.commit()
        return {'message': 'Клиент успешно создан'}

    except Exception as e:
        return {'message': f'Ошибка при создании клиента: {str(e)}'}


# Обновляем баланс клиента
def update_customer_balance(customer_id: int, new_balance: float):
    try:
        db = next(get_db())
        customer = db.query(Customer).filter_by(customer_id=customer_id).first()
        if customer:
            customer.balance = new_balance
            db.commit()
            return {'message': 'Баланс клиента обновлен'}
        else:
            return {'message': 'Клиент не найден'}
    except Exception as e:
        return {'message': f'Ошибка при обновлении баланса клиента: {str(e)}'}


# Удаляем клиента
def delete_customer(customer_id: int):
    try:
        db = next(get_db())
        customer = db.query(Customer).filter_by(customer_id=customer_id).first()
        if customer:
            db.delete(customer)
            db.commit()
            return {'message': 'Клиент успешно удален'}
        else:
            return {'message': 'Клиент не найден'}
    except Exception as e:
        return {'message': f'Ошибка при удалении клиента: {str(e)}'}


# Получаем информацию о клиенте по его ID
def get_customer_info(customer_id: int):
    try:
        db = next(get_db())
        customer = db.query(Customer).filter_by(customer_id=customer_id).first()
        if customer:
            return {
                "id": customer.customer_id,
                "name": customer.name,
                "surname": customer.surname,
                "phone_number": customer.phone_number,
                "address": customer.address,
                "balance": customer.balance
            }
        else:
            return {"message": "Клиент не найден"}
    except Exception as e:
        return {'message': f'Ошибка при получении информации о клиенте: {str(e)}'}


# Получаем список всех клиентов
def get_all_customers():
    try:
        db = next(get_db())
        customers = db.query(Customer).all()
        if customers:
            return [{"id": customer.customer_id, "name": customer.name, "surname": customer.surname} for customer in customers]
        else:
            return []
    except Exception as e:
        return {'message': f'Ошибка при получении списка клиентов: {str(e)}'}
