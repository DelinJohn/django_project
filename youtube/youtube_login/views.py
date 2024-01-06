from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None :
            login(request, user)
            return redirect('home')  # Redirect to home page or desired destination
        else:
            return render(request, 'login_form.html', {'error_message': 'Invalid credentials '})
    else:
        return render(request, 'login_form.html')

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    # ... Your home page logic for logged-in users
    return render(request, 'home.html')
@login_required
def logout_user(request):
    logout(request)
    return redirect('login')