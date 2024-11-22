from pydantic import BaseModel


class OrderCreate(BaseModel):
    smartphone_id: int
    customer_id: int
