# #!/usr/bin/env python
# """Django's command-line utility for administrative tasks."""
# import os
# import sys


# def main():
#     """Run administrative tasks."""
#     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'reading_assessment.settings')
#     try:
#         from django.core.management import execute_from_command_line
#     except ImportError as exc:
#         raise ImportError(
#             "Couldn't import Django. Are you sure it's installed and "
#             "available on your PYTHONPATH environment variable? Did you "
#             "forget to activate a virtual environment?"
#         ) from exc
#     execute_from_command_line(sys.argv)


# if __name__ == '__main__':
#     main()

#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'reading_assessment.settings')
    try:
        from django.core.management import execute_from_command_line
        from django.core.management import call_command
        import django
        django.setup()

        # ✅ Automatically run migrations on every startup (Render safe)
        if os.environ.get('RENDER', 'false') == 'true':  # Detect Render environment
            print("🚀 Running migrations automatically...")
            call_command('migrate')

            # ✅ Auto-create superuser if not already exists
            from django.contrib.auth import get_user_model
            User = get_user_model()
            if not User.objects.filter(username='admin').exists():
                print("👑 Creating default superuser...")
                User.objects.create_superuser(
                    username='admin',
                    email='admin@example.com',
                    password='Admin@123'
                )
            else:
                print("✅ Superuser already exists, skipping creation.")
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
