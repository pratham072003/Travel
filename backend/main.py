from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from routes import tours, users, bookings, whatsapp
from database import Base
from contextlib import asynccontextmanager

# Database setup
DATABASE_URL = "sqlite:///./travel.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables
Base.metadata.create_all(bind=engine)

# Lifespan context
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("Starting Travel API...")
    yield
    # Shutdown
    print("Shutting down...")

# Create FastAPI app
app = FastAPI(
    title="Travel & Tours API",
    description="Beautiful travel booking API",
    version="1.0.0",
    lifespan=lifespan
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(tours.router, prefix="/api/tours", tags=["Tours"])
app.include_router(users.router, prefix="/api/users", tags=["Users"])
app.include_router(bookings.router, prefix="/api/bookings", tags=["Bookings"])
app.include_router(whatsapp.router, prefix="/api/whatsapp", tags=["WhatsApp"])

@app.get("/")
def read_root():
    return {
        "message": "Welcome to Travel & Tours API",
        "docs": "/docs",
        "version": "1.0.0"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
