from pydantic import BaseModel, Field


class CustomerValidator(BaseModel):
    customer_id: int
    name: str
    surname: str
    phone_number: str = Field(..., pattern=r"^\+?\d{10,15}$", description="Номер телефона (между 10 и 15 цифрами)")
    address: str
