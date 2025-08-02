# Payment Gateway Django REST API

A Django REST Framework project for payment processing.

## Project Setup

This project is set up with Django REST Framework and includes:

- Django REST Framework for API development
- CORS headers for cross-origin requests
- Basic user management API
- Health check endpoint
- Admin interface

## Installation

1. Activate the virtual environment:
   ```bash
   .venv\Scripts\activate  # On Windows
   source .venv/bin/activate  # On Linux/Mac
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run migrations:
   ```bash
   python manage.py migrate
   ```

4. Create a superuser (optional):
   ```bash
   python manage.py createsuperuser
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

## API Endpoints

- **Health Check**: `GET /api/health/` - Check if the API is running
- **API Info**: `GET /api/info/` - Get API information and available endpoints
- **Users**: `GET /api/users/` - List all users (requires authentication)
- **Admin**: `/admin/` - Django admin interface

## Admin Credentials

- Username: `admin`
- Password: `admin123`

## API Testing

You can test the API endpoints using:

1. Browser: Visit `http://127.0.0.1:8000/api/health/` for a simple health check
2. Django REST Framework Browsable API: Visit `http://127.0.0.1:8000/api/`
3. Admin Interface: Visit `http://127.0.0.1:8000/admin/`

## Development

The project structure:
```
paymentproject/
├── api/                 # API app
├── paymentproject/      # Main project settings
├── manage.py
└── requirements.txt
```

## Features

- ✅ Django REST Framework setup
- ✅ CORS configuration
- ✅ User management API
- ✅ Health check endpoint
- ✅ Admin interface
- ✅ Database migrations
- ✅ Virtual environment setup
