'use client'

import Image from 'next/image'
import { FiStar, FiCalendar, FiUsers } from 'react-icons/fi'

interface TourCardProps {
  id: number
  title: string
  destination: string
  description: string
  price: number
  duration_days: number
  image_url: string
  rating: number
}

export default function TourCard({
  id,
  title,
  destination,
  description,
  price,
  duration_days,
  image_url,
  rating,
}: TourCardProps) {
  return (
    <div className="card-hover bg-white rounded-lg overflow-hidden shadow-lg border border-gray-100">
      {/* Image */}
      <div className="relative h-48 w-full bg-gray-200">
        <Image
          src={image_url || 'https://images.unsplash.com/photo-1488646953014-85cb44e25828?w=500&h=400&fit=crop'}
          alt={title}
          fill
          className="object-cover"
        />
      </div>

      {/* Content */}
      <div className="p-6">
        {/* Destination Badge */}
        <div className="inline-block bg-blue-100 text-blue-800 px-3 py-1 rounded-full text-sm font-medium mb-3">
          {destination}
        </div>

        {/* Title */}
        <h3 className="text-xl font-bold text-gray-900 mb-2">{title}</h3>

        {/* Description */}
        <p className="text-gray-600 text-sm mb-6 line-clamp-2">{description}</p>

        {/* Price and Button */}
        <div className="flex justify-between items-center">
          <div>
            <p className="text-2xl font-bold text-gray-900">Rs.{price}</p>
            <p className="text-xs text-gray-500">/ km</p>
          </div>
        </div>
      </div>
    </div>
  )
}
