from pydantic import BaseModel


# Валидатор для заказов
class SmartphoneValidator(BaseModel):
    smartphone_id: int
    brand: str
    model: str
    price: float
    description: str