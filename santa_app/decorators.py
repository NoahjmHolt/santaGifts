from django.http import HttpResponse
from django.shortcuts import redirect

def unautherized_access(view_func):
    def wrapper_func(request, *args, **kwargs):

        if request.user.is_authenticated:
          return redirect('items')
        else:
            return view_func(request, *args, **kwargs)
    
    return wrapper_func
