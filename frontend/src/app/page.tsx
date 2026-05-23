"use client"

import { useState, useEffect } from "react"
import Header from "@/components/Header"
import Footer from "@/components/Footer"
import TourCard from "@/components/TourCard"
import { tourAPI } from "@/lib/api"
import { FaWhatsapp } from "react-icons/fa"

interface Tour {
  id: number
  title: string
  destination: string
  description: string
  price: number
  duration_days: number
  image_url: string
  rating: number
}

export default function Home() {
  const [tours, setTours] = useState<Tour[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetchTours()
  }, [])

  const fetchTours = async () => {
    try {
      setLoading(true)
      const response = await tourAPI.getAll(0, 12)
      setTours(response.data)
    } catch (err) {
      console.error("Failed to fetch tours:", err)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <Header />

      <section className="hero-gradient text-white py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <h1 className="text-5xl md:text-6xl font-bold mb-4">Explore the World</h1>
          <p className="text-xl mb-8 text-blue-100">
            Discover unforgettable travel experiences at amazing prices
          </p>

          <div className="max-w-xl mx-auto mt-10 relative group">
            {/* Animated Glow effect behind the card */}
            <div className="absolute -inset-1 bg-gradient-to-r from-green-400 to-[#25D366] rounded-xl blur opacity-25 group-hover:opacity-50 transition duration-1000 group-hover:duration-200"></div>
            
            {/* Main Glassmorphism Card */}
            <div className="relative bg-white/10 backdrop-blur-md border border-white/20 p-8 rounded-xl shadow-2xl transition-transform duration-300 transform group-hover:-translate-y-1">
              <div className="flex flex-col items-center text-center">
                <div className="bg-[#25D366]/20 p-4 rounded-full mb-4 ring-2 ring-[#25D366]/50">
                  <FaWhatsapp className="text-5xl text-[#25D366] animate-pulse" />
                </div>
                
                <h3 className="text-2xl font-bold mb-3 tracking-wide">Contact Us via WhatsApp</h3>
                
                <p className="text-sm md:text-base text-blue-50 mb-8 leading-relaxed px-4">
                  Experience seamless booking and instant support. Click below, send the pre-filled connect message, and then send a quick <strong className="text-white font-semibold">"Hi"</strong> to get started!
                </p>
                
                <a
                  href={`https://api.whatsapp.com/send?phone=14155238886&text=${encodeURIComponent('join move-if')}`}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="w-full sm:w-auto bg-gradient-to-r from-[#25D366] to-[#1DA851] hover:from-[#1DA851] hover:to-[#128C7E] transition-all duration-300 inline-flex items-center justify-center gap-3 px-10 py-4 rounded-full text-white font-bold text-lg shadow-[0_0_15px_rgba(37,211,102,0.5)] hover:shadow-[0_0_25px_rgba(37,211,102,0.7)] transform hover:-translate-y-1"
                >
                  <FaWhatsapp className="text-2xl" />
                  <span>Start Chatting Now</span>
                </a>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section id="tours" className="py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-12">
            <h2 className="text-4xl font-bold text-gray-900 mb-4">Featured Tours</h2>
            <p className="text-xl text-gray-600">Choose from our collection of amazing travel packages</p>
          </div>

          {loading ? (
            <div className="text-center py-12">
              <p className="text-gray-500 text-lg">Loading tours...</p>
            </div>
          ) : tours.length === 0 ? (
            <div className="text-center py-12">
              <p className="text-gray-500 text-lg">No tours available at the moment. Please check back later.</p>
            </div>
          ) : (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
              {tours.map((tour) => (
                <TourCard key={tour.id} {...tour} />
              ))}
            </div>
          )}
        </div>
      </section>

      <section className="bg-white py-20 border-t border-gray-200">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h2 className="text-4xl font-bold text-center mb-12">Why Choose TravelHub?</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div className="text-center">
              <div className="text-4xl mb-4">🌍</div>
              <h3 className="text-xl font-bold mb-2">Global Destinations</h3>
              <p className="text-gray-600">Explore destinations across all continents</p>
            </div>
            <div className="text-center">
              <div className="text-4xl mb-4">💰</div>
              <h3 className="text-xl font-bold mb-2">Best Prices</h3>
              <p className="text-gray-600">Competitive prices and exclusive deals</p>
            </div>
            <div className="text-center">
              <div className="text-4xl mb-4">🎯</div>
              <h3 className="text-xl font-bold mb-2">Easy Booking</h3>
              <p className="text-gray-600">Simple and secure booking process</p>
            </div>
          </div>
        </div>
      </section>

      <Footer />
    </div>
  )
}
