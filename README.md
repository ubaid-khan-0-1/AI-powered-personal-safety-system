# SafeHer – AI-Powered Women Safety & Emergency Alert System

A Flask-based web application designed as an academic demonstration of an AI-assisted women’s safety platform. The current application provides a secure authentication foundation with user registration and login functionality, with the architecture designed to support additional safety features in future development.

---

## Overview

**SafeHer** is designed to provide a foundation for a personal safety platform focused on rapid access, user security, and future AI-assisted emergency capabilities.

The current version focuses on:

* User registration
* Secure user authentication
* Password hashing
* Session-based login management
* Logout functionality
* SQLite database integration
* Responsive authentication pages

Additional safety and AI capabilities can be integrated as the project evolves.

---

## Project Structure

```text
AI-powered-personal-safety-system/
│
├── app.py                    # Main Flask application
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
│
├── instance/
│   └── women_safety.db       # SQLite database
│
├── static/
│   ├── css/                  # Stylesheets
│   └── js/                   # JavaScript files
│
└── templates/
    ├── index.html            # Landing page
    ├── login.html            # Login page
    └── register.html         # Registration page
```

> The SQLite database is automatically created when the application is started.

---

## Features

### Authentication

| Feature                 | Description                                             |
| ----------------------- | ------------------------------------------------------- |
| User Registration       | Allows users to create a new account                    |
| Secure Password Storage | Passwords are stored using Werkzeug password hashing    |
| User Login              | Authenticates registered users using email and password |
| Session Management      | Maintains authenticated user sessions                   |
| Logout                  | Clears the active user session                          |
| Email Validation        | Prevents duplicate email registrations                  |

---

## Authentication Flow

```text
                    ┌─────────────────┐
                    │   Landing Page  │
                    │       /         │
                    └────────┬────────┘
                             │
                  ┌──────────┴──────────┐
                  │                     │
                  ▼                     ▼
           ┌─────────────┐       ┌──────────────┐
           │    Login    │       │  Register    │
           │   /login    │       │  /register   │
           └──────┬──────┘       └───────┬──────┘
                  │                      │
                  │                      ▼
                  │              ┌──────────────┐
                  │              │ Create User  │
                  │              └───────┬──────┘
                  │                      │
                  └──────────┬───────────┘
                             ▼
                    ┌─────────────────┐
                    │ Authenticated   │
                    │     Session     │
                    └─────────────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │     Logout      │
                    │    /logout      │
                    └─────────────────┘
```

---

## Database

The application currently uses **SQLite** with **Flask-SQLAlchemy**.

### User Table

| Column          | Type         | Description                |
| --------------- | ------------ | -------------------------- |
| `id`            | INTEGER      | Primary key                |
| `name`          | VARCHAR(100) | User's full name           |
| `email`         | VARCHAR(150) | Unique email address       |
| `phone`         | VARCHAR(20)  | User's phone number        |
| `password_hash` | VARCHAR(200) | Securely hashed password   |
| `created_at`    | DATETIME     | Account creation timestamp |

### Database Relationship

```text
User
 │
 ├── id
 ├── name
 ├── email
 ├── phone
 ├── password_hash
 └── created_at
```

---

## API & Routes

### Authentication Routes

| Method | Endpoint    | Description               |
| ------ | ----------- | ------------------------- |
| `GET`  | `/`         | Landing page              |
| `GET`  | `/login`    | Display login page        |
| `POST` | `/login`    | Authenticate user         |
| `GET`  | `/register` | Display registration page |
| `POST` | `/register` | Create a new user account |
| `GET`  | `/logout`   | Clear the current session |

---

## Registration

A new user provides:

```text
Name
Email
Phone Number
Password
```

The application validates the submitted information before creating the account.

Passwords are never stored as plain text. They are processed using Werkzeug's password hashing functionality.

```python
generate_password_hash(password)
```

During login, the submitted password is verified against the stored hash:

```python
check_password_hash(
    user.password_hash,
    password
)
```

---

## Login

Users authenticate using:

```text
Email
Password
```

After successful authentication, Flask creates a session containing the user's ID and name.

```python
session['user_id'] = user.id
session['user_name'] = user.name
```

The session can then be cleared through:

```text
/logout
```

---

## Technology Stack

### Backend

* Python 3.x
* Flask
* Flask-SQLAlchemy
* Werkzeug

### Database

* SQLite
* SQLAlchemy ORM

### Frontend

* HTML5
* CSS3
* JavaScript

### Authentication

* Flask Sessions
* Werkzeug Password Hashing

---

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/ubaid-khan-0-1/AI-powered-personal-safety-system.git
```

Navigate into the project:

```bash
cd AI-powered-personal-safety-system
```

---

### 2. Create a Virtual Environment

#### macOS / Linux

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run the Application

#### macOS / Linux

```bash
python3 app.py
```

#### Windows

```bash
python app.py
```

The application will start on:

```text
http://127.0.0.1:5000
```

or:

```text
http://localhost:5000
```

---

## Environment

For development, the application uses:

```text
Python 3.x
Flask
SQLite
```

The SQLite database is automatically initialized when Flask starts.

---

## Security Considerations

The application currently implements basic authentication security through:

* Password hashing
* Unique email validation
* Server-side validation
* Flask session management
* ORM-based database interaction

For production deployment, additional security measures should be implemented, including:

* Environment-based secret keys
* HTTPS
* Secure session cookies
* CSRF protection
* Rate limiting
* Strong password policies
* Input validation and sanitization
* Production WSGI server
* Secure database configuration
* Proper logging and monitoring

---

## Future Enhancements

The project architecture can be extended with additional safety capabilities such as:

* Emergency SOS alerts
* Emergency contact management
* GPS-based location sharing
* Voice-based distress detection
* AI/NLP safety analysis
* Emergency alert generation
* Audio evidence recording
* Alert history
* Push notifications
* SMS and WhatsApp integrations
* Mobile/PWA support
* Wearable and smartwatch integration

These features are planned extensions and are **not part of the current authentication-focused implementation**.

---

## Project Status

**Current Status:** Authentication Module

Implemented:

* [x] Flask application setup
* [x] SQLite database
* [x] User model
* [x] User registration
* [x] Password hashing
* [x] User login
* [x] Session management
* [x] Logout
* [x] Landing page

Planned:

* [ ] Emergency contact management
* [ ] SOS functionality
* [ ] GPS location sharing
* [ ] AI safety analysis
* [ ] VoiceGuard
* [ ] Emergency notifications
* [ ] Alert history
* [ ] Mobile/PWA integration

---

## Disclaimer

SafeHer is an **academic and demonstration project** intended for educational and development purposes.

The current implementation provides authentication functionality and does not constitute a complete emergency response system.

Any future emergency features should be thoroughly tested and integrated with reliable communication services before being considered for real-world safety use.

---

## License

This project is released under the **MIT License**.

See the `LICENSE` file for details.

---

## Author

**Ubaid Khan**

GitHub: `ubaid-khan-0-1`

Project: **AI-powered-personal-safety-system**
