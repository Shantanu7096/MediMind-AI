# 🩺 MediMind AI
### AI-Powered Smart Medicine Reminder & Health Monitoring System

<p align="center">

<img src="static/images/logo.png" width="180">

</p>

---

## 📖 Overview

**MediMind AI** is an AI-powered healthcare management system developed using **Flask, MySQL, Google Gemini AI, EasyOCR, and OpenCV**.

The system helps users manage medicines, receive reminders, monitor health, scan prescriptions using AI, and interact with an intelligent medical assistant.

It is designed to reduce missed medications and improve daily health tracking through Artificial Intelligence and IoT-inspired health monitoring.

---

# 🚀 Features

### 👤 User Management

- User Registration
- Secure Login
- Password Encryption
- Profile Management
- Update Personal Details

---

### 💊 Medicine Management

- Add Medicine
- Edit Medicine
- Delete Medicine
- Search Medicine
- Medicine Status
- Medicine Schedule
- Reminder Time

---

### ⏰ Reminder System

- Daily Medicine Reminder
- Pending Medicines
- Completed Medicines
- Missed Medicines

---

### 🤖 AI Assistant

Powered by **Google Gemini AI**

Features:

- Medicine Explanation
- Health Advice
- Diet Suggestions
- Water Intake Advice
- Sleep Advice
- BMI Guidance
- Medicine Information
- Health FAQs

---

### 📷 Smart Medicine Scanner

Supports **two scanning methods**

#### 1️⃣ EasyOCR

- Printed Prescriptions
- Medicine Strips
- Pharmacy Bills

#### 2️⃣ Gemini Vision

- Handwritten Prescriptions
- Doctor Prescriptions
- Complex Medical Documents

The extracted medicines can be directly saved into the database.

---

### 💧 Water Tracker

- Daily Water Intake
- Water Goal
- Progress Tracking

---

### 😴 Sleep Tracker

- Sleep Duration
- Sleep Quality
- Daily Sleep Record

---

### ⚖ BMI Calculator

- BMI Calculation
- BMI Category
- BMI History

---

### 📊 Dashboard

Shows

- Health Score
- Medicine Statistics
- Today's Medicines
- Today's Reminders
- Water Status
- Sleep Status
- BMI Status
- Health Tips

---

### 📈 Analytics

Health Analytics

- Medicine Statistics
- Water Analytics
- Sleep Analytics
- BMI Analytics

---

### 🔔 Notifications

- Read Notifications
- Delete Notifications
- Notification History

---

# 🛠 Technologies Used

## Backend

- Python
- Flask
- SQLAlchemy
- Flask Login
- Flask Mail

---

## Frontend

- HTML5
- CSS3
- Bootstrap 5
- JavaScript
- Jinja2

---

## Database

- MySQL

---

## Artificial Intelligence

- Google Gemini AI
- EasyOCR
- OpenCV
- NumPy

---

## Tools

- Visual Studio Code
- Git
- GitHub
- MySQL Workbench

---

# 📂 Project Structure

```text
MediMind-AI/

│

├── app.py

├── config.py

├── requirements.txt

├── README.md

├── .env

│

├── ai/

├── models/

├── routes/

├── templates/

├── static/

├── database/

└── instance/
```

---

# ⚙ Installation

## 1 Clone Repository

```bash
git clone https://github.com/Shantanu7096/MediMind-AI.git
```

---

## 2 Open Project

```bash
cd MediMind-AI
```

---

## 3 Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

---

## 4 Install Requirements

```bash
pip install -r requirements.txt
```

---

## 5 Configure Environment Variables

Create a `.env` file.

Example

```env
SECRET_KEY=your_secret_key

MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DB=medimind_ai

GEMINI_API_KEY=your_gemini_api_key

MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_password
MAIL_USE_TLS=True
```

---

## 6 Create Database

Create a MySQL database.

```sql
CREATE DATABASE medimind_ai;
```

Import

```
database/schema.sql
```

---

## 7 Run Project

```bash
python app.py
```

---

# 📱 Modules

✔ Authentication

✔ Dashboard

✔ Medicine Management

✔ Reminder System

✔ AI Chatbot

✔ OCR Scanner

✔ Gemini Vision Scanner

✔ Water Tracker

✔ Sleep Tracker

✔ BMI Calculator

✔ Analytics

✔ Notifications

✔ Profile

✔ Settings

---

# 🧠 AI Workflow

```
User Question

↓

Gemini AI

↓

Health Response
```

---

# 📷 Scanner Workflow

```
Upload Prescription

↓

EasyOCR / Gemini Vision

↓

Medicine Extraction

↓

Medicine Parser

↓

Preview

↓

Save Medicine

↓

Reminder
```

---

# 📊 Dashboard Workflow

```
Login

↓

Dashboard

↓

Medicine

↓

Water

↓

Sleep

↓

BMI

↓

Health Score

↓

Analytics
```

---

# 🔒 Security Features

- Password Hashing
- Session Management
- Login Required Routes
- SQLAlchemy ORM
- CSRF Protection
- Environment Variables

---

# 🎯 Future Scope

- Mobile Application
- Voice Assistant
- Smartwatch Integration
- Cloud Synchronization
- SMS Reminders
- Email Notifications
- PDF Health Reports
- Medicine Barcode Scanner
- Multi-language Support

---

# 📸 Screenshots

Add screenshots here

- Login Page
- Dashboard
- Medicines
- AI Assistant
- OCR Scanner
- Analytics
- Profile
- Settings

---

# 👨‍💻 Developed By

**Shantanu Keraba Patil**

Bachelor of Technology

Computer Science and Technology

---

# 📄 License

This project is developed for educational and academic purposes.

---

# ⭐ Project Status

✅ Authentication Completed

✅ Medicine Management Completed

✅ Reminder System Completed

✅ Dashboard Completed

✅ Water Tracker Completed

✅ Sleep Tracker Completed

✅ BMI Calculator Completed

✅ AI Assistant Completed

✅ OCR Scanner Completed

✅ Gemini Vision Completed

✅ Analytics Completed

✅ Notifications Completed

✅ Profile Completed

✅ Settings Completed

---
