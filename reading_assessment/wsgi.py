# """
# WSGI config for reading_assessment project.

# It exposes the WSGI callable as a module-level variable named ``application``.

# For more information on this file, see
# https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
# """

# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'reading_assessment.settings')

# application = get_wsgi_application()


import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'reading_assessment.settings')
application = get_wsgi_application()

# --------- One-time superuser creation (for Render free tier) ---------
if os.environ.get('CREATE_SUPERUSER', '') == 'True':
    from django.contrib.auth import get_user_model
    User = get_user_model()

    superusers = [
        {"username": "Admin", "email": "admin1@example.com", "password": "Admin@123"},
    ]

    for user in superusers:
        if not User.objects.filter(username=user["username"]).exists():
            print(f"Creating superuser: {user['username']}")
            User.objects.create_superuser(
                username=user["username"],
                email=user["email"],
                password=user["password"]
            )
        else:
            print(f"Superuser {user['username']} already exists.")
