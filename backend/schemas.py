from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str
    full_name: str
    phone: Optional[str] = None

class UserResponse(BaseModel):
    id: int
    email: str
    username: str
    full_name: str
    phone: Optional[str]
    created_at: datetime
    
    class Config:
        from_attributes = True

class TourCreate(BaseModel):
    title: str
    description: str
    destination: str
    price: float
    duration_days: int
    max_travelers: int
    image_url: Optional[str] = None

class TourResponse(BaseModel):
    id: int
    title: str
    description: str
    destination: str
    price: float
    duration_days: int
    max_travelers: int
    image_url: Optional[str]
    rating: float
    created_at: datetime
    
    class Config:
        from_attributes = True

class BookingCreate(BaseModel):
    tour_id: int
    start_date: datetime
    num_travelers: int

class BookingResponse(BaseModel):
    id: int
    user_id: int
    tour_id: int
    booking_date: datetime
    start_date: datetime
    end_date: datetime
    num_travelers: int
    total_price: float
    status: str
    
    class Config:
        from_attributes = True
