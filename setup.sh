#!/bin/bash

echo ""
echo "╔════════════════════════════════════════════════════════════╗"
echo "║       Travel & Tours - Quick Start Setup (macOS/Linux)     ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 is not installed! Download from https://python.org"
    exit 1
fi

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed! Download from https://nodejs.org"
    exit 1
fi

echo "✅ Python and Node.js are installed"
echo ""

# Setup Backend
echo "╔════════════════════════════════════════════════════════════╗"
echo "║            Setting up Backend (FastAPI)...                ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

cd backend

if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing dependencies..."
pip install -q -r requirements.txt

echo ""
echo "✅ Backend setup complete!"
echo ""

# Setup Frontend
echo "╔════════════════════════════════════════════════════════════╗"
echo "║           Setting up Frontend (Next.js)...                ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

cd ../frontend

echo "Installing dependencies..."
npm install --quiet

if [ ! -f ".env.local" ]; then
    echo "Creating .env.local..."
    echo "NEXT_PUBLIC_API_URL=http://localhost:8000" > .env.local
fi

echo ""
echo "✅ Frontend setup complete!"
echo ""

# Display next steps
echo "╔════════════════════════════════════════════════════════════╗"
echo "║              Setup Complete! Next Steps:                   ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""
echo "1️⃣  START BACKEND (new terminal):"
echo "    cd backend"
echo "    source venv/bin/activate"
echo "    uvicorn main:app --reload"
echo "    ➜ API will be at: http://localhost:8000"
echo "    ➜ Docs at: http://localhost:8000/docs"
echo ""
echo "2️⃣  START FRONTEND (new terminal):"
echo "    cd frontend"
echo "    npm run dev"
echo "    ➜ Frontend will be at: http://localhost:3000"
echo ""
echo "3️⃣  Open browser:"
echo "    http://localhost:3000"
echo ""
echo "📚 Documentation:"
echo "    - SETUP_GUIDE.md - Detailed setup instructions"
echo "    - HOSTING_GUIDE.md - Deployment & hosting options"
echo "    - ARCHITECTURE.md - System architecture overview"
echo ""
