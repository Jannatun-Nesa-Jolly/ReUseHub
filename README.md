# ReUseHub ♻️

**Campus Reuse & Donation Network** — a Django prototype that helps students list reusable items, discover affordable pre-owned goods, exchange items, and donate things they no longer need.

## Features
- Student registration, login, and logout
- Create, edit, browse, and complete item listings
- Listing types: sale, exchange, and donation
- Search by keyword and filter by category, condition, and listing type
- Optional item image uploads (Pillow)
- Save/unsave items
- Report listings for administrator review
- Django admin dashboard for categories, listings, and reports
- Owner-only listing edits and completion controls

## Technology
- Python 3.10+
- Django 5.x
- SQLite (local development)
- HTML, CSS, minimal JavaScript-free frontend
- Pillow for image uploads

## Run locally

```bash
# 1. Create and activate a virtual environment
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create database tables
python manage.py makemigrations marketplace
python manage.py migrate

# 4. Create an admin account
python manage.py createsuperuser

# 5. Start the development server
python manage.py runserver
```

Open http://127.0.0.1:8000/ for the website and http://127.0.0.1:8000/admin/ for administration.

## First-time setup
Add categories such as Books, Electronics, Clothing, Accessories, and Study Materials from the Django admin panel before posting listings.

## Project structure

```text
ReUseHub/
├── config/                 # Django project settings and URLs
├── marketplace/            # Listings, profiles, saved items, reports
│   ├── migrations/
│   ├── templates/
│   └── static/marketplace/
├── manage.py
├── requirements.txt
└── README.md
```

## Scope and limitations
This is a campus marketplace prototype. Users coordinate collection directly. It does not include online payments, courier integration, or automatic identity verification. Contact information should only be shared when a user chooses to provide it.

## Before deployment
- Replace `SECRET_KEY` with an environment variable.
- Set `DEBUG = False` and configure `ALLOWED_HOSTS`.
- Configure production static/media storage and HTTPS.
- Review contact-sharing and privacy requirements.
- Consider PostgreSQL for production deployment.

## Academic project
Prepared for the ReUseHub Python/Django project proposal: a campus-focused platform for reuse, exchange, and donation.
