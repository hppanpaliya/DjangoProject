# DjangoProject
## Django Login System

A Django-based user authentication system implementing signup, login, and user management functionality through REST APIs.

## Project Description

This project implements a basic user authentication system with the following features:
- User registration and login 
- User profile management via CRUD operations
- Form-based authentication with Django forms
- Bootstrap for frontend styling

### Screenshots
See all screenshots in the [screenshots folder](https://github.com/hppanpaliya/DjangoProject/tree/main/screenshots#readme):

## Setup

1. Create and activate virtual environment:
```bash
python -m venv ~/.virtualenv/DjangoAssignment
source ~/.virtualenv/DjangoAssignment/bin/activate
```

2. Install Django and run migrations:
```bash
pip install django
python manage.py migrate
```

3. Run the server:
```bash
python manage.py runserver
```

### API Endpoints

1. Authentication:
- `GET /` - Test endpoint (Hello World)
- `POST /signup/` - Register new user
- `POST /login/` - Authenticate user

2. User Management:
- `GET /users/` - List all users
- `GET /users/<email>/` - Get specific user
- `PUT /users/<email>/` - Update user
- `DELETE /users/<email>/` - Delete user
