from database import Base
from sqlalchemy import Column, Integer, String, Float, Boolean

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)  # Primary key
    date = Column(String)
    description = Column(String)
    amount = Column(Float)
    category = Column(String)
    is_income = Column(Boolean)
