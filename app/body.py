from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime
from .models import ServiceCreate, Status

#PYDANTIC validators

#Schema for inserting data
class Customer(BaseModel):
    name: str
    email: EmailStr
    password: str
    address: str

class Service(BaseModel):
    type: ServiceCreate
    total_cost: Optional[float] = 0

class ValidProduct(BaseModel):
    name: str
    description: str
    price: float
    stock_quantity: int

class Variant(BaseModel):
    size: str
    color: str
    stock_quantity: int

class Repair(BaseModel):
    description: str
    status: Optional[Status] = Status.PENDING

class ItemRequest(BaseModel):
    product_variant_id: int
    quantity: int
    unit_price: float


#Token
class Token(BaseModel):
    access_token: str
    token_type: str
    customer_id: int
   
class TokenData(BaseModel):
    id: Optional[int] = None