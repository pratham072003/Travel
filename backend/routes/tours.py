from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Tour
from schemas import TourCreate, TourResponse
from typing import List

router = APIRouter()

@router.get("/", response_model=List[TourResponse])
def get_all_tours(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """Get all available tours with pagination"""
    tours = db.query(Tour).offset(skip).limit(limit).all()
    return tours

@router.get("/{tour_id}", response_model=TourResponse)
def get_tour(tour_id: int, db: Session = Depends(get_db)):
    """Get specific tour details"""
    tour = db.query(Tour).filter(Tour.id == tour_id).first()
    if not tour:
        raise HTTPException(status_code=404, detail="Tour not found")
    return tour

@router.get("/destination/{destination}", response_model=List[TourResponse])
def get_tours_by_destination(destination: str, db: Session = Depends(get_db)):
    """Get all tours for a specific destination"""
    tours = db.query(Tour).filter(Tour.destination.ilike(f"%{destination}%")).all()
    return tours

@router.post("/", response_model=TourResponse)
def create_tour(tour: TourCreate, db: Session = Depends(get_db)):
    """Create a new tour (admin only)"""
    db_tour = Tour(**tour.dict())
    db.add(db_tour)
    db.commit()
    db.refresh(db_tour)
    return db_tour
