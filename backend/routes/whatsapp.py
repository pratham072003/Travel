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

WELCOME_MESSAGE = """Welcome to Travel Hub! 🚗✨

Thank you for choosing us for your travel needs. My name is Gaurav, and I’m here to make your journey comfortable, safe, and hassle-free.

At Travel Hub, we provide reliable and well-maintained car services for all your travel requirements, including local trips, outstation travel, airport transfers, family tours, business travel, and customized travel packages. Our focus is on punctuality, comfort, and excellent customer service to ensure you have a smooth travel experience.

For any bookings, inquiries, or assistance, feel free to contact me anytime at 9811867707.

Looking forward to serving you and making your journey memorable!

Gaurav
Travel Hub
📞 9811867707"""

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
