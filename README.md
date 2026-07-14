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
  <img width="1892" height="972" alt="image" src="https://github.com/user-attachments/assets/6e5559f1-64fe-40fb-9409-48924d792b2d" />

  <img width="1862" height="846" alt="image" src="https://github.com/user-attachments/assets/42bcc1df-481b-46a5-be09-6ac8e4703b1f" />

  <img width="1707" height="870" alt="image" src="https://github.com/user-attachments/assets/f7a28bb4-f115-4d55-9714-d138bd1109ee" />

  
- Dashboard
  <img width="1896" height="973" alt="image" src="https://github.com/user-attachments/assets/6bf21c36-e224-47a0-b889-05db60a60df9" />

  <img width="1895" height="966" alt="image" src="https://github.com/user-attachments/assets/bc470f8e-8927-4aa9-be7f-a1f6f2b689ed" />

- Medicines
  <img width="1906" height="807" alt="image" src="https://github.com/user-attachments/assets/63f59f6c-c726-413f-b2a9-fdff71422690" />

  <img width="1897" height="727" alt="image" src="https://github.com/user-attachments/assets/0bc48287-7ffb-4cd5-819e-2bb6fc06566e" />

- AI Assistant
  <img width="1896" height="862" alt="image" src="https://github.com/user-attachments/assets/50694e0c-b0ed-4169-a075-c92272ffba04" />

- OCR Scanner
  <img width="1896" height="942" alt="image" src="https://github.com/user-attachments/assets/af5c0c90-fbc5-439f-8bac-0d0aa12a6a6d" />

  <img width="1407" height="921" alt="image" src="https://github.com/user-attachments/assets/b64fd75f-a37b-4ab4-97c1-53e02a0dd809" />

- Analytics
  <img width="1907" height="931" alt="image" src="https://github.com/user-attachments/assets/7e16497e-c785-4f34-9188-2e1b9ad7c03c" />

  <img width="1877" height="802" alt="image" src="https://github.com/user-attachments/assets/1c33d8b8-d739-4560-9cbb-fa8595878c4a" />

- Profile
  <img width="1272" height="970" alt="image" src="https://github.com/user-attachments/assets/f6fbdaea-46c2-49bc-ab8a-e2fd3eb3cda9" />

- Settings
  <img width="1910" height="868" alt="image" src="https://github.com/user-attachments/assets/abe63f54-4bde-4f39-b581-10e93ea99de7" />

  <img width="1897" height="967" alt="image" src="https://github.com/user-attachments/assets/7bdfbbf5-5e91-4b0c-9810-a749a0cd65ec" />



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
