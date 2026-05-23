import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'Travel & Tours - Explore the World',
  description: 'Discover amazing travel destinations and book your next adventure',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className="bg-white">{children}</body>
    </html>
  )
}
