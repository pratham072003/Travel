from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import Response
from pydantic import BaseModel
import os

try:
    from twilio.rest import Client
    from twilio.twiml.messaging_response import MessagingResponse
except ImportError:
    Client = None
    MessagingResponse = None

router = APIRouter()

class WhatsAppRequest(BaseModel):
    user_phone: str
    message: str | None = None

WELCOME_MESSAGE = """🦅 Welcome to Eagle Tour and Travel! 🚗✨

Thank you for contacting us. We provide comfortable cars and travellers for family trips, vacations, outstation travel, weddings, and group tours.

Planning a trip? Just share:
📍 Pickup Location & Destination
📅 Travel Date
👨‍👩‍👧‍👦 Number of Passengers

We’ll help you find the best vehicle at the best price for a safe and comfortable journey 😊

📞 Call/WhatsApp: +91 8368253267
📧 Email: gauravsharma4116@gmail.com

🦅 Eagle Tour and Travel, Comfortable Journeys, Happy Memories!"""

@router.post("/send")
def send_whatsapp(payload: WhatsAppRequest):
    """Send a WhatsApp message to the provided phone number using Twilio."""
    if Client is None:
        raise HTTPException(status_code=500, detail="Twilio client not installed")

    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    from_number = os.getenv("TWILIO_WHATSAPP_FROM")

    if not account_sid or not auth_token or not from_number:
        raise HTTPException(status_code=500, detail="Twilio credentials not configured")

    client = Client(account_sid, auth_token)

    to = payload.user_phone
    if not to.startswith("whatsapp:"):
        to = f"whatsapp:{to}"

    from_whatsapp = from_number
    if not from_whatsapp.startswith("whatsapp:"):
        from_whatsapp = f"whatsapp:{from_whatsapp}"

    body = payload.message or WELCOME_MESSAGE

    try:
        msg = client.messages.create(body=body, from_=from_whatsapp, to=to)
        return {"sid": msg.sid, "status": msg.status}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to send message: {str(e)}")

@router.post("/webhook")
async def whatsapp_webhook(request: Request):
    """Webhook to handle incoming WhatsApp messages and auto-reply."""
    if MessagingResponse is None:
        raise HTTPException(status_code=500, detail="Twilio not installed")
        
    # We can read the incoming message if needed
    # form_data = await request.form()
    # incoming_msg = form_data.get('Body', '').lower()
    
    # Create TwiML response to send back automatically
    response = MessagingResponse()
    response.message(WELCOME_MESSAGE)
    
    return Response(content=str(response), media_type="application/xml")
