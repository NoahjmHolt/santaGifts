from django.http import HttpResponse
from django.shortcuts import redirect

def unautherized_access(view_func):
    def wrapper_func(request, *args, **kwargs):

        if request.user.is_authenticated:
          return redirect('items')
        else:
            return view_func(request, *args, **kwargs)
    
    return wrapper_func


def allowed_users(allowed_groups=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            print('working: ', allowed_groups)

            return view_func(request, *args, **kwargs)
        
        return wrapper_func
    
    return decorator
