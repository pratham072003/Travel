from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Booking, Tour
from schemas import BookingCreate, BookingResponse
from datetime import datetime, timedelta
from typing import List

router = APIRouter()

@router.post("/", response_model=BookingResponse)
def create_booking(booking: BookingCreate, user_id: int, db: Session = Depends(get_db)):
    """Create a new booking"""
    # Get tour
    tour = db.query(Tour).filter(Tour.id == booking.tour_id).first()
    if not tour:
        raise HTTPException(status_code=404, detail="Tour not found")
    
    # Calculate end date
    end_date = booking.start_date + timedelta(days=tour.duration_days)
    total_price = tour.price * booking.num_travelers
    
    # Create booking
    db_booking = Booking(
        user_id=user_id,
        tour_id=booking.tour_id,
        start_date=booking.start_date,
        end_date=end_date,
        num_travelers=booking.num_travelers,
        total_price=total_price,
        status="pending"
    )
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking

@router.get("/{booking_id}", response_model=BookingResponse)
def get_booking(booking_id: int, db: Session = Depends(get_db)):
    """Get booking details"""
    booking = db.query(Booking).filter(Booking.id == booking_id).first()
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking

@router.get("/user/{user_id}", response_model=List[BookingResponse])
def get_user_bookings(user_id: int, db: Session = Depends(get_db)):
    """Get all bookings for a user"""
    bookings = db.query(Booking).filter(Booking.user_id == user_id).all()
    return bookings
