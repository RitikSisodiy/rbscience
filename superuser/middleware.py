from django.contrib.auth import REDIRECT_FIELD_NAME
from django.shortcuts import redirect
from django.urls import resolve
def simple_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        r = resolve(request.path)
        if r._func_path[:r._func_path.find('.')] in ["superuser"]: #add app name IN LIST  to APPLY middleware in that app
            if request.user.is_superuser:
                response = get_response(request)
            else:
                response = redirect('index')
        else:
            response = get_response(request)
        return response
    return middleware