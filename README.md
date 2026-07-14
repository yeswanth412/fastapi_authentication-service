# 🔐 FastAPI Authentication Service

A production-ready authentication backend built with **FastAPI**, **MongoDB**, **JWT**, and **SMTP Email Verification**.

This project demonstrates how to build a secure authentication system using modern backend development practices, including user registration, login, email verification, password reset, JWT authentication, and protected API routes.


## 🚀 Features

- ✅ User Registration
- ✅ User Login
- ✅ JWT Authentication
- ✅ Access & Refresh Tokens
- ✅ Email Verification
- ✅ Forgot Password
- ✅ Reset Password
- ✅ Password Hashing using bcrypt
- ✅ Protected Routes
- ✅ MongoDB Integration
- ✅ Repository Pattern Architecture
- ✅ Environment Variable Configuration
- ✅ Interactive Swagger API Documentation


## 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| FastAPI | Backend Framework |
| MongoDB | Database |
| JWT | Authentication |
| Pydantic | Data Validation |
| Passlib + bcrypt | Password Hashing |
| SMTP | Email Verification |
| Uvicorn | ASGI Server |


## 📁 Project Structure

```text
auth_service/
│
├── app/
│   ├── core/
│   ├── database/
│   ├── dependencies/
│   ├── repositories/
│   ├── routes/
│   ├── schemas/
│   ├── services/
│   ├── utils/
│   └── main.py
│
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
└── main.py
```


## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/yeswanth412/fastapi_authentication-service.git
```

### Navigate to the project

```bash
cd fastapi_authentication-service
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

**macOS/Linux**

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure environment variables

Copy:

```text
.env.example
```

to

```text
.env
```

and update the values.

### Run the server

```bash
uvicorn main:app --reload
```



### Open Swagger

```
http://127.0.0.1:8000/docs
```

## 📌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /register | Register a new user |
| POST | /login | Authenticate user |
| GET | /profile | Get authenticated user profile |
| POST | /refresh | Refresh access token |
| POST | /logout | Logout user |
| GET | /verify-email | Verify email address |
| POST | /forgot-password | Send password reset email |
| POST | /reset-password | Reset user password |


## 📚 What I Learned

Through this project, I gained hands-on experience with:

- Building REST APIs using FastAPI
- Implementing JWT Authentication
- Secure password hashing using bcrypt
- Email verification using SMTP
- Password reset workflows
- Repository Pattern architecture
- MongoDB CRUD operations
- Environment variable management
- API documentation with Swagger UI



## 🚀 Future Improvements

- Google OAuth 2.0 Login
- GitHub OAuth Login
- Docker support
- Redis for token blacklisting
- Unit and integration testing
- CI/CD with GitHub Actions
- Role-Based Access Control (RBAC)