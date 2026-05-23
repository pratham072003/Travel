from sqlalchemy import Column, Integer, String, Float, DateTime, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    password_hash = Column(String)
    full_name = Column(String)
    phone = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    bookings = relationship("Booking", back_populates="user")

class Tour(Base):
    __tablename__ = "tours"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    destination = Column(String, index=True)
    price = Column(Float)
    duration_days = Column(Integer)
    max_travelers = Column(Integer)
    image_url = Column(String, nullable=True)
    rating = Column(Float, default=0.0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    bookings = relationship("Booking", back_populates="tour")

class Booking(Base):
    __tablename__ = "bookings"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    tour_id = Column(Integer, ForeignKey("tours.id"))
    booking_date = Column(DateTime, default=datetime.utcnow)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    num_travelers = Column(Integer)
    total_price = Column(Float)
    status = Column(String, default="pending")  # pending, confirmed, cancelled
    
    user = relationship("User", back_populates="bookings")
    tour = relationship("Tour", back_populates="bookings")
