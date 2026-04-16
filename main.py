from fastapi import FastAPI
from pydantic import BaseModel,EmailStr
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env")

app = FastAPI()

conf = ConnectionConfig(
    MAIL_USERNAME=os.getenv("BREVO_LOGIN_USERNAME"),
    MAIL_PASSWORD=os.getenv("BREVO_SMTP_KEY"),
    MAIL_FROM=os.getenv("MAIL_FROM"),
    MAIL_PORT=int(os.getenv("MAIL_PORT")),
    MAIL_SERVER=os.getenv("BREVO_MAIL_SERVER"),

    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,

    USE_CREDENTIALS=True
)

class EmailRequest(BaseModel):
    email: EmailStr
    subject: str
    message: str

@app.post("/email")
async def send_email(req:EmailRequest):
    message = MessageSchema(
        subject=req.subject,
        recipients=[req.email],
        body=req.message,
        subtype="html"
    )
    fm = FastMail(conf)
    await fm.send_message(message)

    return {"status": "Email sent successfully"}