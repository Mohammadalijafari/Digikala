Digikala

A Django-based e-commerce web application inspired by Digikala, Iran's largest online marketplace. The project models core marketplace functionality — user accounts, product listings, and sellers — as separate Django apps.

Tech Stack
Django 5.2 — web framework
Pillow — image handling (product/media uploads)
PostgreSQL — database (per repo topics; configure via Django settings)
Dev tooling — black, isort, pylint, mypy for formatting/linting
Project Structure
Digikala/
├── accounts/       # User authentication & account management
├── digikala/       # Project settings, root URLs, WSGI/ASGI config
├── products/       # Product catalog app
├── sellers/        # Seller/vendor management app
├── static/         # Static assets (CSS, JS, images)
├── templates/       # HTML templates
├── manage.py
└── requirements.txt
Getting Started
Prerequisites
Python 3.10+
pip
PostgreSQL (or update digikala/settings.py to use SQLite for local dev)
Installation
bash
git clone https://github.com/Mohammadalijafari/Digikala.git
cd Digikala
python -m venv venv
source venv/bin/activate   # on Windows: venv\Scripts\activate
pip install -r requirements.txt
Configure the database

Update the DATABASES setting in digikala/settings.py with your PostgreSQL credentials, or swap in SQLite for quick local testing.

Run migrations & start the server
bash
python manage.py migrate
python manage.py createsuperuser   # optional, for admin access
python manage.py runserver

The app will be available at http://127.0.0.1:8000/.

Apps Overview
App	Responsibility
accounts	User registration, login, and account management
products	Product catalog — listing, details, categories
sellers	Seller/vendor profiles and management
digikala	Project-level configuration (settings, root URLconf)
Contributing

Contributions, issues, and feature requests are welcome. Feel free to open a pull request or issue.
