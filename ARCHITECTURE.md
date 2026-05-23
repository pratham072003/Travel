# 🏗️ Architecture Overview

## System Design

```
┌─────────────────────────────────────────────────────────┐
│                     Internet                             │
└──────┬──────────────────────────────────────────┬────────┘
       │                                          │
   [Vercel]                                  [Railway]
   Frontend                                  Backend
   Next.js                                   FastAPI
       │                                          │
       └──────────────────┬───────────────────────┘
                          │ (API Calls)
                          ▼
                      REST API
                   (JSON over HTTP)
                          │
                    ┌─────┴─────┐
                    ▼           ▼
              Database       Files
             (SQLite/PostgreSQL)


                   
## Technology Stack

### Frontend
- **Framework:** Next.js 14 (React)
- **Styling:** Tailwind CSS
- **State Management:** Zustand
- **HTTP Client:** Axios
- **Icons:** React Icons
- **Language:** TypeScript

### Backend
- **Framework:** FastAPI
- **Server:** Uvicorn
- **Database:** SQLAlchemy ORM with SQLite (PostgreSQL for prod)
- **Validation:** Pydantic
- **Authentication:** JWT (ready to implement)
- **Password:** bcrypt
- **Language:** Python 3.11+

### Hosting
- **Frontend:** Vercel (CDN + Serverless)
- **Backend:** Railway / Render (PaaS)
- **Database:** SQLite (dev) → PostgreSQL (prod)
- **DNS:** Custom domain (optional)

## API Architecture

```
                    ┌─────────────┐
                    │  FastAPI    │
                    │   Server    │
                    └──────┬──────┘
                           │
            ┌──────────────┼──────────────┐
            ▼              ▼              ▼
         Tours          Users         Bookings
        Router          Router        Router
            │              │              │
            └──────────┬───┴──────┬──────┘
                       │          │
                ┌──────▼──────────▼─────┐
                │    SQLAlchemy ORM     │
                │    (Models/Schema)    │
                └──────────┬────────────┘
                           │
                    ┌──────▼──────┐
                    │  SQLite DB  │
                    │  (travel.db)│
                    └─────────────┘
```

## Data Flow

### Creating a Booking

```
User Interface (Next.js)
    │
    └─► POST /api/bookings
        {tour_id, num_travelers, start_date}
        │
        ▼
FastAPI Backend
    ├─► Validate data (Pydantic)
    ├─► Calculate total price
    ├─► Create booking record
    └─► Return booking details
        │
        ▼
Database
    └─► Save booking to SQLite

    
    ▼
Frontend receives confirmation
    └─► Show success message
    └─► Update UI
```

### Fetching Tours

```
User Interface (Next.js)
    │
    └─► GET /api/tours?skip=0&limit=10
        │
        ▼
FastAPI Backend
    ├─► Query database
    ├─► Apply filters/pagination
    └─► Return list of tours
        │
        ▼
Database
    └─► Fetch matching records

    
    ▼
Frontend receives tours
    └─► Render tour cards
    └─► Handle loading states
```

## Scalability Path

### Phase 1: Current (Free Tier)
- SQLite database
- Single backend instance
- Vercel frontend

### Phase 2: Growth
- Migrate to PostgreSQL
- Add caching (Redis)
- Load balancing

### Phase 3: Scale
- Microservices architecture
- Kubernetes deployment
- Advanced analytics
- Admin dashboard

## Security Considerations

✅ **Implemented:**
- CORS configuration
- Pydantic validation
- Password hashing (bcrypt)

🔜 **To Add:**
- JWT authentication
- Rate limiting
- Input sanitization
- SQL injection prevention (already handled by ORM)
- HTTPS/SSL
- Environment variable secrets
- Database encryption

