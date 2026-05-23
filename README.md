# 🌍 Travel & Tours Website

A modern, beautiful, and fully functional travel booking platform built with **FastAPI** (Python backend) and **Next.js** (React frontend).

![Architecture](https://img.shields.io/badge/Architecture-Full%20Stack-blue)
![Frontend](https://img.shields.io/badge/Frontend-Next.js%2014-black)
![Backend](https://img.shields.io/badge/Backend-FastAPI-green)
![Database](https://img.shields.io/badge/Database-SQLite%20%2F%20PostgreSQL-blue)
![Hosting](https://img.shields.io/badge/Hosting-Vercel%20%2B%20Railway-blueviolet)

---

## 🎯 Features

### ✨ Frontend (Next.js + Tailwind CSS)
- 🎨 Beautiful, responsive design
- 🔍 Tour search and filtering
- 📱 Mobile-friendly interface
- ⚡ Fast page loads with Next.js optimization
- 🌈 Modern UI components
- 🔐 User authentication ready

### 🔧 Backend (FastAPI)
- 📡 RESTful API with automatic documentation
- 🗄️ SQLAlchemy ORM with SQLite/PostgreSQL
- ✔️ Pydantic data validation
- 🔐 Password hashing with bcrypt
- 🌐 CORS enabled for frontend
- 📊 Tour management system
- 👥 User management
- 📅 Booking system

### 🚀 Deployment Ready
- One-click deployment to Vercel (frontend)
- Simple deployment to Railway (backend)
- Environment variable management
- Production-ready configurations

---

## 📦 Project Structure

```
travel/
├── backend/                 # FastAPI Python application
│   ├── main.py             # Application entry point
│   ├── models.py           # Database models
│   ├── schemas.py          # Pydantic schemas
│   ├── database.py         # DB configuration
│   ├── routes/             # API endpoints
│   │   ├── tours.py
│   │   ├── users.py
│   │   └── bookings.py
│   └── requirements.txt
│
├── frontend/               # Next.js React application
│   ├── src/
│   │   ├── app/           # Pages & layouts
│   │   ├── components/    # React components
│   │   ├── lib/           # Utilities & API
│   │   └── styles/
│   ├── public/            # Static files
│   ├── package.json
│   └── next.config.js
│
├── SETUP_GUIDE.md         # Detailed setup instructions
├── HOSTING_GUIDE.md       # Deployment options
├── ARCHITECTURE.md        # System architecture
├── setup.bat              # Windows quick setup
└── setup.sh               # macOS/Linux quick setup
```

---

## ⚡ Quick Start

### Option 1: Windows (One-Click Setup)

1. Double-click `setup.bat`
2. Follow the prompts
3. It will install all dependencies automatically

### Option 2: macOS/Linux

```bash
chmod +x setup.sh
./setup.sh
```

### Option 3: Manual Setup

See [SETUP_GUIDE.md](SETUP_GUIDE.md) for detailed instructions.

---

## 🚀 Running Locally

### Start Backend (Terminal 1)

```bash
cd backend
python -m venv venv
source venv/Scripts/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

**API available at:** `http://localhost:8000`
**Documentation:** `http://localhost:8000/docs`

### Start Frontend (Terminal 2)

```bash
cd frontend
npm install
npm run dev
```

**Frontend available at:** `http://localhost:3000`

---

## 🌐 Hosting & Deployment

### Recommended: Vercel + Railway (Free/Low Cost)

#### Frontend → Vercel
- ✅ Free tier
- ✅ Optimized for Next.js
- ✅ Global CDN

#### Backend → Railway
- ✅ $5/month free credit
- ✅ Easy deployment
- ✅ PostgreSQL included

**See [HOSTING_GUIDE.md](HOSTING_GUIDE.md) for detailed deployment steps.**

### Other Options
- **Render:** All-in-one platform
- **AWS:** Enterprise-grade
- **Google Cloud / Azure:** Advanced features
- **Fly.io:** Developer-friendly

---

## 📋 API Documentation

### Base URL
```
http://localhost:8000 (local)
https://your-railway-app.railway.app (production)
```

### Available Endpoints

#### Tours
```
GET    /api/tours              # Get all tours
GET    /api/tours/{id}         # Get tour details
GET    /api/tours/destination/{destination}  # Search by destination
POST   /api/tours              # Create tour (admin)
```

#### Users
```
POST   /api/users/register     # Register new user
GET    /api/users/{id}         # Get user details
```

#### Bookings
```
POST   /api/bookings           # Create booking
GET    /api/bookings/{id}      # Get booking
GET    /api/bookings/user/{user_id}  # Get user's bookings
```

**Interactive docs:** Visit `http://localhost:8000/docs`

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| **Frontend** | Next.js 14, React 18, TypeScript, Tailwind CSS |
| **Backend** | FastAPI, Python 3.11+, SQLAlchemy, Pydantic |
| **Database** | SQLite (dev), PostgreSQL (prod) |
| **Authentication** | bcrypt, JWT ready |
| **Frontend Hosting** | Vercel |
| **Backend Hosting** | Railway / Render |
| **Package Managers** | npm (frontend), pip (backend) |

---

## 📱 Features in Detail

### Search Tours
Users can search tours by destination with real-time filtering.

### Tour Details
Complete information including:
- Tour description
- Duration and pricing
- Ratings and reviews
- Traveler capacity
- Beautiful images

### Booking System
- Select tour and dates
- Specify number of travelers
- Automatic price calculation
- Booking confirmation

### User Authentication
- Register new account
- Login/logout
- Profile management
- Booking history

---

## 🔒 Security Features

✅ **Implemented:**
- Password hashing with bcrypt
- CORS configuration
- Input validation with Pydantic
- SQL injection prevention (SQLAlchemy ORM)

🔜 **To Add:**
- JWT token authentication
- Rate limiting
- HTTPS/SSL
- Database encryption
- Environment secrets management

---

## 📈 Scalability

### Current (SQLite)
- Good for: Development, testing, small deployments
- Limitations: Single connection, no real concurrency

### Recommended (PostgreSQL)
- Good for: Production, multiple users
- Benefits: Concurrent connections, better performance

### Enterprise (Multi-tier)
- Microservices architecture
- Redis caching
- Load balancing
- Kubernetes deployment

---

## 🧪 Testing API

### Using Swagger UI (Recommended)
Visit: `http://localhost:8000/docs`

### Using Postman
1. Download [Postman](https://postman.com)
2. Create requests for each endpoint
3. Test different scenarios

### Using cURL
```bash
# Get all tours
curl http://localhost:8000/api/tours

# Get specific tour
curl http://localhost:8000/api/tours/1

# Create tour (requires JSON body)
curl -X POST http://localhost:8000/api/tours \
  -H "Content-Type: application/json" \
  -d '{"title":"Paris Tour","destination":"Paris","description":"Explore Paris","price":999,"duration_days":5,"max_travelers":20}'
```

---

## 📚 Documentation Files

- **[SETUP_GUIDE.md](SETUP_GUIDE.md)** - Detailed local & deployment setup
- **[HOSTING_GUIDE.md](HOSTING_GUIDE.md)** - Hosting platforms comparison
- **[ARCHITECTURE.md](ARCHITECTURE.md)** - System design & technical architecture
- **[backend/README.md](backend/README.md)** - Backend documentation
- **[frontend/README.md](frontend/README.md)** - Frontend documentation

---

## 🚦 Next Steps

### Phase 1: Development
- [ ] Run locally
- [ ] Test all endpoints
- [ ] Customize designs
- [ ] Add more tours

### Phase 2: Enhancement
- [ ] Add JWT authentication
- [ ] Implement payment gateway (Stripe/Razorpay)
- [ ] Add email notifications
- [ ] Create admin dashboard

### Phase 3: Deployment
- [ ] Deploy backend to Railway
- [ ] Deploy frontend to Vercel
- [ ] Configure custom domain
- [ ] Set up monitoring & logging

### Phase 4: Growth
- [ ] Migrate to PostgreSQL
- [ ] Add caching (Redis)
- [ ] Implement analytics
- [ ] Add advanced features

---

## 💡 Customization

### Change Colors
Edit `frontend/tailwind.config.ts`:
```js
colors: {
  primary: '#3B82F6',      // Change these
  secondary: '#10B981',
  accent: '#F59E0B',
}
```

### Add Your Content
1. Add tours to database
2. Update company info in footer
3. Customize home page copy

### Add Features
- Reviews & ratings
- Wishlist
- Admin panel
- Email notifications

---

## 🐛 Troubleshooting

### Backend won't start
```bash
# Check Python version
python --version  # Should be 3.11+

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall

# Check port availability
netstat -ano | findstr :8000  # Windows
lsof -i :8000  # macOS/Linux
```

### Frontend won't connect to backend
- Check `NEXT_PUBLIC_API_URL` in `.env.local`
- Ensure backend is running
- Check browser console for CORS errors

### Database errors
- Delete `travel.db` to reset
- Clear any old migrations
- Reinstall SQLAlchemy

---

## 📞 Support

For issues:
1. Check [SETUP_GUIDE.md](SETUP_GUIDE.md)
2. Review error logs
3. Test with Swagger UI (`/docs`)
4. Check environment variables

---

## 📄 License

This project is open source and available for personal and commercial use.

---

## 🌟 Key Highlights

✨ **Modern Stack** - Latest versions of FastAPI and Next.js
🎨 **Beautiful UI** - Tailwind CSS with responsive design
⚡ **Fast Performance** - Optimized for speed
🚀 **Easy Deployment** - One-click hosting setup
📱 **Mobile Ready** - Works on all devices
🔒 **Secure** - Industry-standard security practices
📊 **Scalable** - Ready to grow with your business

---

## 🎯 Start Building Today! 

```bash
# Quick start
./setup.bat           # Windows
./setup.sh           # macOS/Linux

# Or manual setup
cd backend && pip install -r requirements.txt
cd ../frontend && npm install
```

Then follow the prompts and visit `http://localhost:3000`!

---

**Made with ❤️ for travel enthusiasts! Happy traveling! ✈️🌍**
