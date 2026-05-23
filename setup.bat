@echo off
echo.
echo ╔════════════════════════════════════════════════════════════╗
echo ║       Travel & Tours - Quick Start Setup (Windows)         ║
echo ╚════════════════════════════════════════════════════════════╝
echo.

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python is not installed! Download from https://python.org
    pause
    exit /b 1
)

:: Check if Node.js is installed
node --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Node.js is not installed! Download from https://nodejs.org
    pause
    exit /b 1
)

echo ✅ Python and Node.js are installed
echo.

:: Setup Backend
echo ╔════════════════════════════════════════════════════════════╗
echo ║            Setting up Backend (FastAPI)...                ║
echo ╚════════════════════════════════════════════════════════════╝
echo.

cd backend

if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Installing dependencies...
pip install -q -r requirements.txt

echo.
echo ✅ Backend setup complete!
echo.

:: Setup Frontend
echo ╔════════════════════════════════════════════════════════════╗
echo ║           Setting up Frontend (Next.js)...                ║
echo ╚════════════════════════════════════════════════════════════╝
echo.

cd ..\frontend

echo Installing dependencies...
call npm install --quiet

if not exist .env.local (
    echo Creating .env.local...
    echo NEXT_PUBLIC_API_URL=http://localhost:8000 > .env.local
)

echo.
echo ✅ Frontend setup complete!
echo.

:: Display next steps
echo ╔════════════════════════════════════════════════════════════╗
echo ║              Setup Complete! Next Steps:                   ║
echo ╚════════════════════════════════════════════════════════════╝
echo.
echo 1️⃣  START BACKEND (new terminal):
echo    cd backend
echo    venv\Scripts\activate
echo    uvicorn main:app --reload
echo    ➜ API will be at: http://localhost:8000
echo    ➜ Docs at: http://localhost:8000/docs
echo.
echo 2️⃣  START FRONTEND (new terminal):
echo    cd frontend
echo    npm run dev
echo    ➜ Frontend will be at: http://localhost:3000
echo.
echo 3️⃣  Open browser:
echo    http://localhost:3000
echo.
echo 📚 Documentation:
echo    - SETUP_GUIDE.md - Detailed setup instructions
echo    - HOSTING_GUIDE.md - Deployment & hosting options
echo    - ARCHITECTURE.md - System architecture overview
echo.
pause
