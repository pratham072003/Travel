'use client'

import { useState } from 'react'
import { FiMenu, FiX, FiMessageCircle } from 'react-icons/fi'
import { whatsappAPI } from '@/lib/api'

export default function Header() {
  const [isOpen, setIsOpen] = useState(false)
  const [showModal, setShowModal] = useState(false)
  const [userPhone, setUserPhone] = useState('')
  const DEFAULT_HEADER_MESSAGE = "Hello! I'm interested in booking a tour. Please contact me."
  const [sending, setSending] = useState(false)
  const [statusMsg, setStatusMsg] = useState<string | null>(null)

  return (
    <header className="sticky top-0 z-50 bg-white shadow-sm">
      <nav className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16 items-center">
          {/* Logo */}
          <div className="flex-shrink-0">
            <a href="/" className="text-2xl font-bold text-blue-600">
              ✈️ TravelHub
            </a>
          </div>

          {/* Desktop Menu */}
          <div className="hidden md:flex space-x-8">
            <a href="#tours" className="text-gray-700 hover:text-blue-600 transition">
              Tours
            </a>
            <a href="#contact" className="text-gray-700 hover:text-blue-600 transition">
              Contact
            </a>
          </div>

          {/* Contact Button */}
          <div className="hidden md:flex space-x-4 items-center">
            <button
              onClick={() => setShowModal(true)}
              className="flex items-center gap-2 text-gray-700 hover:text-blue-600"
            >
              <FiMessageCircle /> Chat Now
            </button>
          </div>

          {/* Mobile Menu Button */}
          <button className="md:hidden" onClick={() => setIsOpen(!isOpen)}>
            {isOpen ? <FiX size={24} /> : <FiMenu size={24} />}
          </button>
        </div>

        {/* Mobile Menu */}
        {isOpen && (
          <div className="md:hidden pb-4 space-y-2">
            <a href="#tours" className="block py-2 text-gray-700 hover:text-blue-600">
              Tours
            </a>
            <a href="#contact" className="block py-2 text-gray-700 hover:text-blue-600">
              Contact
            </a>
            <button
              onClick={() => setShowModal(true)}
              className="w-full btn-primary mt-4 block text-center"
            >
              Chat on WhatsApp
            </button>
          </div>
        )}
      
      {showModal && (
        <div className="fixed inset-0 z-50 flex items-center justify-center">
          <div className="absolute inset-0 bg-black opacity-50" onClick={() => setShowModal(false)} />
          <div className="bg-white rounded-lg shadow-xl z-10 max-w-md w-full p-6">
            <h3 className="text-lg font-semibold mb-2">Chat with TravelHub</h3>
            <p className="text-sm text-gray-600 mb-4">Enter your WhatsApp number and we will message you from our number.</p>
            <input
              type="tel"
              placeholder="Your WhatsApp number (with country code, e.g. +15551234567)"
              value={userPhone}
              onChange={(e) => setUserPhone(e.target.value)}
              className="w-full rounded border px-3 py-2 mb-3"
            />
            {statusMsg && <p className="text-sm mb-2">{statusMsg}</p>}
            <div className="flex justify-end gap-2">
              <button className="px-4 py-2" onClick={() => setShowModal(false)} disabled={sending}>Cancel</button>
              <button
                className="btn-primary px-4 py-2"
                onClick={async () => {
                    if (!userPhone.trim()) {
                      setStatusMsg('Please enter your phone number.')
                      return
                    }
                    try {
                      setSending(true)
                      setStatusMsg(null)
                      await whatsappAPI.send(userPhone.trim(), DEFAULT_HEADER_MESSAGE)
                      setStatusMsg('Message sent successfully.')
                      setUserPhone('')
                      setShowModal(false)
                    } catch (err: any) {
                      setStatusMsg('Failed to send message.')
                    } finally {
                      setSending(false)
                    }
                  }}
              >
                {sending ? 'Sending...' : 'Send Message'}
              </button>
            </div>
          </div>
        </div>
      )}
      </nav>
    </header>
  )
}
