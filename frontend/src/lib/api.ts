import axios from 'axios'

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'

const api = axios.create({
  baseURL: `${API_URL}/api`,
  headers: {
    'Content-Type': 'application/json',
  },
})

export const tourAPI = {
  getAll: (skip = 0, limit = 10) => api.get(`/tours/?skip=${skip}&limit=${limit}`),
  getById: (id: number) => api.get(`/tours/${id}`),
  getByDestination: (destination: string) => api.get(`/tours/destination/${destination}`),
  create: (data: any) => api.post('/tours', data),
}

export const userAPI = {
  register: (data: any) => api.post('/users/register', data),
  getById: (id: number) => api.get(`/users/${id}`),
}

export const bookingAPI = {
  create: (data: any, userId: number) => api.post(`/bookings?user_id=${userId}`, data),
  getById: (id: number) => api.get(`/bookings/${id}`),
  getUserBookings: (userId: number) => api.get(`/bookings/user/${userId}`),
}

export const whatsappAPI = {
  send: (user_phone: string, message?: string) => api.post('/whatsapp/send', { user_phone, message }),
}

export default api
