from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
from database import SessionLocal, engine
from models import Base, Transaction
from pydantic import BaseModel
from datetime import datetime

# App initialization
app = FastAPI(title="Finance Tracker API", version="1.0")

# CORS configuration
origins = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database setup
Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic schemas
class TransactionBase(BaseModel):
    date: str
    description: str
    amount: float
    category: str
    is_income: bool

class TransactionResponse(TransactionBase):
    id: int

    class Config:
        orm_mode = True

# Routes
@app.post("/transactions/", response_model=TransactionResponse)
def create_transaction(transaction: TransactionBase, db: Session = Depends(get_db)):
    try:
        db_transaction = Transaction(**transaction.dict())
        db.add(db_transaction)
        db.commit()
        db.refresh(db_transaction)
        return db_transaction
    except Exception as e:
        raise HTTPException(status_code=500, detail="Transaction creation failed")

@app.get("/transactions/", response_model=List[TransactionResponse])
def get_transactions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Transaction).order_by(Transaction.date.desc()).offset(skip).limit(limit).all()
@app.get("/")
def root():
    return {"message": "Welcome to the Finance Tracker API!"}
