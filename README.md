# 🏦 BM Banking: Full-Stack Web Application

A professional, secure banking web application built with **Python (Flask)** and **PostgreSQL**. This project demonstrates a complete cloud-deployed web service, featuring real-time data persistence and a modern, responsive GUI.

[🌐 **Live Demo on Render**](https://bank-9bdp.onrender.com/)

## 🚀 Key Features

- **Secure Web Authentication**: Implements session-based login with username and 4-digit PIN validation.
- **Cloud Data Persistence**: Fully integrated with **Neon PostgreSQL**, ensuring all user balances and accounts are stored securely in the cloud.
- **Real-time Transactions**: Supports instant deposits and withdrawals with automated server-side balance updates.
- **Robust Error Handling**: Custom logic to prevent overdrafts, enforce minimum deposits ($20), and handle duplicate username registrations.

## 🛠️ Tech Stack

- **Backend**: Python 3, Flask
- **Database**: PostgreSQL (Cloud-hosted via **Neon**)
- **Frontend**: HTML5, CSS3 (Custom GUI)
- **Deployment**: Render (Web Service), GitHub (Version Control)
- **Libraries**: `psycopg2-binary`, `python-dotenv`, `gunicorn`

## ⚙️ Engineering Workflow

1.  **Architecture**: The app uses a functional Flask backend that communicates with a PostgreSQL relational database through optimized SQL queries.
2.  **Security**: Credentials are managed via `os.environ`, ensuring the `DATABASE_URL` is never exposed in the public repository.
3.  **Deployment**: Configured with a `requirements.txt` and a customized Start Command on Render to bridge the gap between local development on macOS and cloud production.

## 🧠 Skills Demonstrated

- **Full-Stack Development**: Connecting a Python backend to a dynamic HTML/CSS frontend.
- **Cloud Infrastructure**: Managing cloud databases (Neon) and web hosting platforms (Render).
- **Database Design**: Implementing CRUD (Create, Read, Update) operations and maintaining data integrity.

---
