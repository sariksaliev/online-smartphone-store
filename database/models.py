from sqlalchemy import Column, Integer, String, Float, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from database import Base


class Customer(Base):
    __tablename__ = "customer"

    customer_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)  # Ограничение длины до 50 символов
    surname = Column(String(50), nullable=False)  # Ограничение длины до 50 символов
    phone_number = Column(String(15), unique=True)  # Используем String для телефонов
    address = Column(String(255))  # Адрес с ограничением до 255 символов
    balance = Column(Numeric(10, 2), default=0.00)  # Используем Numeric для точности денежных сумм

    # Связь с заказами
    orders = relationship("Order", back_populates="customer")  # Оптимизированный lazy loading


class Smartphone(Base):
    __tablename__ = "smartphones"

    id = Column(Integer, primary_key=True)
    brand = Column(String(50), nullable=False)  # Ограничение на длину бренда
    model = Column(String(50), nullable=False)  # Ограничение на длину модели
    description = Column(String(255), nullable=True)  # Описание до 255 символов
    price = Column(Float, nullable=False)

    # Связь с заказами
    orders = relationship("Order", back_populates="smartphone")  # Двусторонняя связь


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customer.customer_id"), nullable=False)  # Исправлен ForeignKey
    smartphone_id = Column(Integer, ForeignKey("smartphones.id"), nullable=False)

    # Связи с клиентом и смартфоном
    customer = relationship("Customer", back_populates="orders")
    smartphone = relationship("Smartphone", back_populates="orders")
