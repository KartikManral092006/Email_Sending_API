# 📧 FastAPI Email Notification API

A simple and production-ready email notification service built using **FastAPI** and **Brevo (SMTP)**.

---

##  Features

* Send email notifications via API
* Async email sending
* HTML email support
* Environment-based configuration
* Clean and minimal FastAPI setup

---

## Tech Stack

* **FastAPI** – Web framework
* **FastAPI-Mail** – Email handling
* **Brevo (Sendinblue)** – SMTP provider
* **Python-dotenv** – Environment management

---

##  Project Structure

```
NotificationAPI/
│
├── main.py
├── .env
├── requirements.txt
└── README.md
```

---

##  Setup Guide

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd NotificationAPI
```

---

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

---

### 3. Install Dependencies

```bash
pip install fastapi uvicorn fastapi-mail python-dotenv
```

---

### 4. Configure Environment Variables

Create a `.env` file:

```env
BREVO_MAIL_USERNAME=your_smtp_login
BREVO_SMTP_KEY=your_smtp_key
MAIL_FROM=your_verified_email
BREVO_MAIL_SERVER=smtp-relay.brevo.com
MAIL_PORT=587
```

---

## ▶️ Running the Server

```bash
uvicorn main:app --reload
```

Open in browser:

```
http://127.0.0.1:8000/docs
```

---

##  API Endpoint

### POST `/email`

Send an email notification.

#### Request Body:

```json
{
  "email": "receiver@example.com",
  "subject": "Hello ",
  "message": "<h2>This is a test email</h2>"
}
```

---

## Response

```json
{
  "status": "Email sent successfully"
}
```

---


##  Author

**Kartik Manral**

---

