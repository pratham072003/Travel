# Travel & Tours Frontend

Modern Next.js frontend for travel booking platform.

## Features

- ✨ Beautiful, responsive design with Tailwind CSS
- 🚀 Next.js 14 with App Router
- 🎨 Modern UI components
- 🔍 Search functionality
- 📱 Mobile-friendly
- ⚡ Fast and optimized

## Setup

1. Install dependencies:
```bash
npm install
```

2. Create `.env.local`:
```
NEXT_PUBLIC_API_URL=http://localhost:8000
```

3. Run development server:
```bash
npm run dev
```

Visit `http://localhost:3000`

## Build for Production

```bash
npm run build
npm start
```

## Deployment

### Deploy to Vercel (Recommended)

1. Push code to GitHub
2. Connect repository at [vercel.com](https://vercel.com)
3. Set environment variable: `NEXT_PUBLIC_API_URL` to your backend URL
4. Deploy!

## Project Structure

- `src/app/` - Pages and layouts
- `src/components/` - Reusable components
- `src/lib/` - Utilities and API calls
- `public/` - Static assets

