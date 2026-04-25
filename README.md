# eCommerce Backend — DevelopersHub Internship

## Live Demo
https://shopnow-ainie.onrender.com

## Tech Stack
- Backend: Python 3.10, Django 5.2
- Database: PostgreSQL (Neon)
- Frontend: HTML5, CSS3, Django Templates
- Deployment: Render.com

## Features
- Home page with featured products
- Product listing with search and category filters
- Product detail pages
- Server-side search by name or category
- Pagination — 9 products per page
- User authentication — login, signup, logout
- Protected routes — add product requires login
- Add Product form
- Fully responsive — desktop and mobile
- Django admin panel

## Setup Instructions
```bash
git clone https://github.com/ainieworks/ecommerce-backend-design.git
cd ecommerce-backend-design
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata products.json
python manage.py createsuperuser
python manage.py runserver
```

## Weekly Progress
- ✅ Week 1 — Django setup, static pages, responsive templates
- ✅ Week 2 — PostgreSQL, Product model, dynamic content, search
- ✅ Week 3 — Auth, pagination, add product, deployed live