# 🚀 Blog CRM Backend API

> A production-ready backend built with **FastAPI**, **PostgreSQL**, and **SQLModel** featuring secure JWT authentication, role-based authorization, Blog Management, Mini CRM, File Uploads, Email Notifications, and interactive Swagger documentation.

<p align="center">

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![SQLModel](https://img.shields.io/badge/SQLModel-Database-green?style=for-the-badge)
![JWT](https://img.shields.io/badge/JWT-Authentication-black?style=for-the-badge)
![Swagger](https://img.shields.io/badge/Swagger-API%20Docs-85EA2D?style=for-the-badge&logo=swagger)

</p>

---

# ✨ Features

## 🔐 Authentication & Security

- JWT Authentication
- Secure Password Hashing (bcrypt)
- Role-Based Access Control (Admin/User)
- Protected API Routes
- Welcome Email after Registration
- Login Notification Email

---

## 👤 User Management

- Register User
- Login User
- Get Current User
- Update Profile
- Get All Users (Admin)
- Get User by ID (Admin)
- Delete User (Admin)

---

## 📝 Blog Management

- Create Blog
- Update Blog
- Delete Blog
- Get All Blogs
- Get Blog by ID
- Blog Categories
- Blog Comments

---

## 📂 Category Management

- Create Category
- Update Category
- Delete Category
- View Categories

---

## 💬 Comment System

- Add Comments
- Update Comments
- Delete Comments
- View Comments by Blog

---

## 📈 Mini CRM

### Lead Management

- Create Lead
- Update Lead
- Delete Lead
- View Leads
- Personal Lead Ownership

### Notes

- Create Notes
- Update Notes
- Delete Notes
- Lead Notes Management

---

## 📎 File Upload

- Upload PDF
- Upload JPG
- Upload PNG
- File Type Validation
- Static File Serving

---

## 📧 Email Service

- Gmail SMTP Integration
- Welcome Email
- Login Alert Email
- Reusable Email Utility

---

# 🏗️ Project Architecture

```
                Client

                  │

                  ▼

             FastAPI Router

                  │

                  ▼

        Business Logic Layer

                  │

                  ▼

         SQLModel ORM Models

                  │

                  ▼

            PostgreSQL Database
```

---

# 📁 Project Structure

```text
app/
│
├── auth.py
├── database.py
├── dependencies.py
├── main.py
│
├── models/
│   ├── user.py
│   ├── blog_post.py
│   ├── category.py
│   ├── comment.py
│   ├── lead.py
│   └── note.py
│
├── routers/
│   ├── auth.py
│   ├── user.py
│   ├── blog.py
│   ├── lead.py
│   ├── note.py
│   └── upload.py
│
├── schemas/
│   ├── userschemas.py
│   ├── blogpostschemas.py
│   ├── categoryschemas.py
│   ├── commentschemas.py
│   ├── leadschemas.py
│   └── noteschemas.py
│
└── services/
    └── email_utils.py
```

---

# 🗄️ Database Models

- User
- BlogPost
- Category
- Comment
- Lead
- Note

---

# 🔗 Relationships

- User → Blog Posts
- User → Comments
- User → Leads
- User → Notes
- Category → Blog Posts
- Blog → Comments
- Lead → Notes

---

# 📌 API Modules

| Module | Status |
|---------|--------|
| Authentication | ✅ |
| Users | ✅ |
| Categories | ✅ |
| Blogs | ✅ |
| Comments | ✅ |
| Leads | ✅ |
| Notes | ✅ |
| Upload | ✅ |
| Email Service | ✅ |

---

# 🔑 Authentication Flow

```
Register User

      │

Hash Password

      │

Store User

      │

Login

      │

Generate JWT

      │

Protected Routes
```

---

# ⚙️ Installation

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git

cd YOUR_REPOSITORY

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

---

# 🔐 Environment Variables

Create a `.env` file.

```env
DATABASE_URL=

SECRET_KEY=

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=60

SMTP_EMAIL=

SMTP_PASSWORD=

SMTP_SERVER=smtp.gmail.com

SMTP_PORT=587
```

---

# 📄 API Documentation

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# 📸 Screenshots

Add screenshots of:

- Swagger UI
- PostgreSQL Database
- File Upload API
- Email Notification
- Project Folder Structure

---

# 🚀 Future Improvements

- Docker
- Redis Cache
- Background Tasks
- Search & Filtering
- Pagination
- Unit Testing
- CI/CD Pipeline
- AI Integration
- Docker Compose
- Cloud Deployment

---

# 🛠️ Tech Stack

- Python
- FastAPI
- SQLModel
- PostgreSQL
- JWT Authentication
- Pydantic
- SMTP
- Swagger/OpenAPI

---

# 👨‍💻 Author

**Najmul Huda**

Backend Developer | Python | FastAPI | PostgreSQL

GitHub:
https://github.com/00najmulhuda

---

⭐ If you found this project useful, consider giving it a star!