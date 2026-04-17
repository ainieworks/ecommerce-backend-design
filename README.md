# eCommerce Backend — DevelopersHub Internship

A full-stack eCommerce web application built with Django and PostgreSQL.

## Tech Stack
- **Backend:** Python 3.10, Django 5.2
- **Database:** PostgreSQL
- **Frontend:** HTML5, CSS3, Django Templates
- **Deployment:** Render.com (Week 3)

## Features
- Home page with featured in-stock products
- Product listing page with search and category filters
- Product detail page with stock status
- Server-side search by name or category
- Fully responsive — desktop and mobile
- Django admin panel for product management
- User authentication (Week 3)
- Pagination (Week 3)

## Setup Instructions

```bash
# Clone the repo
git clone https://github.com/ainieworks/ecommerce-backend-design.git
cd ecommerce-backend-design

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Configure PostgreSQL
# Create a database named ecommerce_db
# Update DATABASES in ecommerce/settings.py with your credentials

# Run migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Start server
python manage.py runserver
```

## Weekly Progress
- ✅ Week 1 — Django setup, static pages, responsive templates
- ✅ Week 2 — PostgreSQL, Product model, dynamic content, search
- ⏳ Week 3 — Authentication, pagination, deployment