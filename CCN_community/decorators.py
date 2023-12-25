from django.shortcuts import redirect

def superuser(function):
    def wrap(request, *args, **kwargs):
        # Check if user is authenticated, if not, redirect to login page
        if not request.user.is_superuser:
            return redirect('home')  # Redirect to your login page URL name

        # If user is authenticated, execute the original view function
        return function(request, *args, **kwargs)

    return wrap
