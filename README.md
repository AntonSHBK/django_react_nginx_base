# django_react_nginx_base
Base project for work with  Django and React

# Building
Development build:

`docker-compose build`

`docker-compose up`

Production build:

`docker-compose -f docker-compose.prod.yml build`

`docker-compose -f docker-compose.prod.yml up`

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
