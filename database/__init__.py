from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Путь к БД
SQLALCHEMY_DATABASE_URI = 'sqlite:///restik.db'
# Создаем наш движок
engine = create_engine(SQLALCHEMY_DATABASE_URI)
# Соединения
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()