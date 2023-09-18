# django_react_nginx_base

## About Project
Base project for work with  Django and React

- Django
- Gunicorn
- React.js
- Postgres
- Nginx
- Celery
- Docker
- Docker Compose

# Building
Development build:
```bush
docker-compose build
docker-compose up
```

Production build:
```
docker-compose -f docker-compose.prod.yml build
docker-compose -f docker-compose.prod.yml up
```

Djanngo settings loacte in `backend/app/settings/settings.py`

```
├── __init__.py
├── asgi.py
├── settings
│   ├── __init__.py
│   ├── common_settings.py
│   ├── dev_settings.py
│   ├── prod_settings.py
│   └── settings.py
├── urls.py
└── wsgi.py
```

Python requirments locate in pip_install_txt folder.

Connect to portal:
http://127.0.0.1:8000

Connect to react:
http://localhost:3000/

Write by Anton Pisarenko
