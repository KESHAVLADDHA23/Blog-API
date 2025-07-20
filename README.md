# 📝 Blog API

A RESTful Blog API built using FastAPI. This backend service supports user authentication, blog creation, updating, deleting, and retrieving posts, along with proper permission handling.

---

## 🚀 Features

- 🔐 JWT-based User Authentication (Register/Login)
- ✍️ CRUD operations for Blog Posts
- 👥 User-based Access Control
- 📄 Swagger and Redoc API Documentation (Auto-generated)
- 💾 SQLite/MySQL compatible via SQLAlchemy ORM
- 🧪 Testable and modular code structure

---

## 🛠️ Tech Stack

- **Framework**: FastAPI
- **ORM**: SQLAlchemy
- **Authentication**: OAuth2 + JWT
- **Database**: SQLite (default) or MySQL/PostgreSQL
- **Documentation**: Swagger UI / Redoc (auto from FastAPI)

## 📦 Project Setup

### 🔧 Requirements

- Python 3.8+
- pip

### ⬇️ Installation

```bash
# Clone the repo
git clone https://github.com/KESHAVLADDHA23/Blog-API.git
cd Blog-API

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the API
uvicorn main:app --reload


Project Structure-
Blog-API/
├── main.py               # Entry point for FastAPI
├── models.py             # SQLAlchemy models
├── schemas.py            # Pydantic schemas
├── database.py           # DB connection and session
├── routers/              # Modular route handling
│   ├── blog.py
│   └── user.py
├── auth/                 # Authentication logic
│   ├── hashing.py
│   └── token.py
├── requirements.txt
└── README.md
