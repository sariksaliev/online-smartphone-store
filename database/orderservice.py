from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import Session
from database.models import Order, Smartphone


def creation_new_order(db: Session, smartphone_id: int, customer_id: int):
    try:
        existing_order = db.query(Order).filter_by(customer_id=customer_id, smartphone_id=smartphone_id).first()
        if existing_order:
            return {"status": "error", "message": "Такой заказ уже существует"}

        new_order = Order(customer_id=customer_id, smartphone_id=smartphone_id)
        db.add(new_order)
        db.commit()
        db.refresh(new_order)

        return {"status": "success", "data": new_order}
    except IntegrityError:
        db.rollback()
        return {"status": "error", "message": "Ошибка при добавлении заказа. Проверьте данные."}
    except Exception as e:
        db.rollback()
        return {"status": "error", "message": str(e)}


def delete_order(db: Session, order_id: int):
    try:
        order = db.query(Order).filter_by(id=order_id).first()
        if not order:
            return {"status": "error", "message": "Заказ не найден"}
        db.delete(order)
        db.commit()
        return {"status": "success", "message": "Заказ успешно удалён"}
    except SQLAlchemyError as e:
        db.rollback()
        return {"status": "error", "message": f"Ошибка при удалении заказа: {str(e)}"}


def get_all_orders(db: Session):
    try:
        all_orders = db.query(Order).all()
        if not all_orders:
            return {"status": "error", "message": "Нет доступных заказов"}
        return {"status": "success", "data": all_orders}
    except SQLAlchemyError as e:
        return {"status": "error", "message": f"Ошибка при получении всех заказов: {str(e)}"}


def update_order(db: Session, order_id: int, new_smartphone_id: int):
    try:
        order = db.query(Order).filter_by(id=order_id).first()
        if not order:
            return {"status": "error", "message": "Заказ не найден"}
        order.smartphone_id = new_smartphone_id
        db.commit()
        return {"status": "success", "message": "Заказ успешно обновлён"}
    except SQLAlchemyError as e:
        db.rollback()
        return {"status": "error", "message": f"Ошибка при обновлении заказа: {str(e)}"}


def get_order_by_id(db: Session, order_id: int):
    try:
        order = db.query(Order).filter_by(id=order_id).first()
        if not order:
            return {"status": "error", "message": "Заказ не найден"}
        return {"status": "success", "data": order}
    except SQLAlchemyError as e:
        return {"status": "error", "message": f"Ошибка при получении заказа: {str(e)}"}


def all_orders(db: Session, customer_id: int):
    try:
        orders = (
            db.query(Order)
            .filter_by(customer_id=customer_id)
            .join(Smartphone, Order.smartphone_id == Smartphone.id)
            .all()
        )
        if orders:
            return {
                "status": "success",
                "data": [
                    {
                        "order_id": order.id,
                        "customer_id": order.customer_id,
                        "smartphone": {
                            "id": order.smartphone.id,
                            "brand": order.smartphone.brand,
                            "model": order.smartphone.model,
                            "price": order.smartphone.price,
                        },
                    }
                    for order in orders
                ],
            }
        else:
            return {"status": "error", "message": "У клиента нет заказов"}
    except Exception as e:
        return {"status": "error", "message": f"Ошибка при получении заказов клиента: {str(e)}"}
