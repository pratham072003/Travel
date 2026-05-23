# Travel & Tours Website - Complete Setup Guide

A modern, full-stack travel booking platform built with FastAPI (backend) and Next.js (frontend).

## 🚀 Project Structure

```
travel/
├── backend/          # FastAPI Python backend
│   ├── main.py       # Application entry point
│   ├── models.py     # Database models
│   ├── schemas.py    # Pydantic validation schemas
│   ├── database.py   # Database configuration
│   ├── routes/       # API endpoints
│   │   ├── tours.py
│   │   ├── users.py
│   │   └── bookings.py
│   └── requirements.txt
│
└── frontend/         # Next.js React frontend
    ├── src/
    │   ├── app/      # Pages and layouts
    │   ├── components/  # React components
    │   ├── lib/      # Utilities and API calls
    │   └── styles/
    ├── package.json
    └── next.config.js
```

## 🛠️ Local Development Setup

### Backend Setup (Python)

1. Navigate to backend folder:
```bash
cd backend
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/Scripts/activate  # Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the server:
```bash
uvicorn main:app --reload
```

**API will be available at:**
- Base URL: `http://localhost:8000`
- API Docs: `http://localhost:8000/docs` (Swagger UI)
- ReDoc: `http://localhost:8000/redoc`

### Frontend Setup (Node.js)

1. Navigate to frontend folder:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Create `.env.local`:
```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

4. Run development server:
```bash
npm run dev
```

**Frontend will be available at:** `http://localhost:3000`

---

## 📋 API Endpoints

### Tours
- `GET /api/tours` - Get all tours
- `GET /api/tours/{id}` - Get specific tour
- `GET /api/tours/destination/{destination}` - Search tours by destination
- `POST /api/tours` - Create new tour (admin)

### Users
- `POST /api/users/register` - Register new user
- `GET /api/users/{id}` - Get user details

### Bookings
- `POST /api/bookings` - Create booking
- `GET /api/bookings/{id}` - Get booking details
- `GET /api/bookings/user/{user_id}` - Get user's bookings

---

## 🌐 Hosting Recommendations

### **Option 1: Vercel + Railway (Recommended for Free Tier)**

#### Frontend: Vercel
**Cost:** Free tier with generous limits
- Optimized for Next.js
- Automatic deployments from GitHub
- Global CDN
- Serverless functions

**Steps:**
1. Push code to GitHub
2. Go to [vercel.com](https://vercel.com)
3. Click "New Project"
4. Select your GitHub repository
5. Set environment variables:
   - `NEXT_PUBLIC_API_URL` = your Railway backend URL
6. Deploy!

#### Backend: Railway
**Cost:** Free tier ($5/month credit)
- Simple deployment
- Environment variables management
- Database hosting
- Easy scaling

**Steps:**
1. Go to [railway.app](https://railway.app)
2. Click "New Project"
3. Select "Deploy from GitHub"
4. Choose your backend repository
5. Add environment variables:
   - `DATABASE_URL` = provided by Railway
6. Set Python version to 3.11+
7. Add service startup command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
8. Deploy!

---

### **Option 2: Render (All-in-One Alternative)**

**Cost:** Free tier available (limited), paid plans start at $7/month

**Frontend:**
1. Go to [render.com](https://render.com)
2. Create new Static Site
3. Connect GitHub
4. Build command: `npm run build`
5. Publish directory: `.next`

**Backend:**
1. Create new Web Service
2. Connect GitHub backend repository
3. Environment: Python 3.11
4. Build command: `pip install -r requirements.txt`
5. Start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`

---

### **Option 3: AWS (Most Features, Paid)**

**Cost:** Free tier limited, pay-as-you-go after

**Frontend (S3 + CloudFront):**
- Static hosting on S3
- CDN via CloudFront

**Backend (EC2 or Elastic Beanstalk):**
- EC2: Virtual server control
- Elastic Beanstalk: Managed deployment

---

### **Option 4: Google Cloud / Azure**

Similar to AWS with competitive pricing and free tier options.

---

## 🔑 Key Features

### Backend (FastAPI)
- ✅ RESTful API with FastAPI
- ✅ SQLAlchemy ORM with SQLite
- ✅ Pydantic validation
- ✅ CORS enabled
- ✅ Automatic API documentation
- ✅ Password hashing with bcrypt
- ✅ User authentication ready

### Frontend (Next.js)
- ✅ Modern React with TypeScript
- ✅ Tailwind CSS styling
- ✅ Responsive design
- ✅ Beautiful UI components
- ✅ API integration ready
- ✅ State management with Zustand
- ✅ Image optimization
- ✅ Search functionality

---

## 📝 Next Steps to Enhance

1. **Authentication:**
   - Add JWT tokens
   - Implement login/registration pages
   - Protected routes

2. **Payment Integration:**
   - Stripe or Razorpay integration
   - Booking confirmation

3. **Notifications:**
   - Email confirmations
   - SMS alerts
   - Push notifications

4. **Admin Dashboard:**
   - Tour management
   - Booking analytics
   - User management

5. **Advanced Features:**
   - Reviews and ratings
   - Wishlist functionality
   - Social sharing
   - Real-time chat support

---

## 🚀 Deployment Checklist

### Before Deploying:
- [ ] Update CORS origins in backend
- [ ] Set production environment variables
- [ ] Build frontend for production
- [ ] Test API endpoints
- [ ] Add error handling
- [ ] Set up logging
- [ ] Add database backups

### Production Configs:
- [ ] Set `DEBUG=False` in FastAPI
- [ ] Use PostgreSQL instead of SQLite
- [ ] Add SSL/HTTPS
- [ ] Set up monitoring
- [ ] Configure CDN for static files

---

## 📞 Support

For issues or questions:
1. Check API docs at `/docs`
2. Review error logs
3. Verify environment variables
4. Test with Postman/Insomnia

---

**Happy traveling! 🌍✈️**
