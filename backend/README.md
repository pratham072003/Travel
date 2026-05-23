# Travel & Tours Backend API

Backend API built with FastAPI for a travel booking platform.

## Setup

1. Create virtual environment:
```bash
python -m venv venv
source venv/Scripts/activate  # Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the server:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`
- API Docs: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Project Structure

- `main.py` - FastAPI application entry point
- `database.py` - Database configuration
- `models.py` - SQLAlchemy models
- `schemas.py` - Pydantic schemas for validation
- `routes/` - API route handlers

## Deployment

For Railway or Render:
1. Connect your GitHub repository
2. Set Python version to 3.11+
3. Build command: `pip install -r requirements.txt`
4. Start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`

