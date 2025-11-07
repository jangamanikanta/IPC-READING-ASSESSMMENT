import base64
import os
from django.http import HttpResponse

EXEMPT_PATHS = (
    '/static/',
    '/health',
    '/healthz',
    '/favicon.ico',
)

def basic_auth_middleware(get_response):
    def middleware(request):
        # Skip these paths
        for p in EXEMPT_PATHS:
            if request.path.startswith(p):
                return get_response(request)

        username = os.environ.get('BASIC_AUTH_USERNAME')
        password = os.environ.get('BASIC_AUTH_PASSWORD')

        if not username or not password:
            return get_response(request)

        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if auth_header:
            try:
                auth_method, auth_b64 = auth_header.split(' ', 1)
                if auth_method.lower() == 'basic':
                    decoded = base64.b64decode(auth_b64).decode('utf-8')
                    user, pw = decoded.split(':', 1)
                    if user == username and pw == password:
                        return get_response(request)
            except Exception:
                pass

        response = HttpResponse('Authentication required', status=401)
        response['WWW-Authenticate'] = 'Basic realm="Restricted Area"'
        return response

    return middleware
