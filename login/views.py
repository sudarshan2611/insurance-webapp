from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
# from django.contrib.auth.decorators import login_required

def LoginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home after successful login
        else:
            return render(request, 'login/login_page.html', {'error': 'Invalid credentials'})
    return render(request, 'login/login_page.html')

# @login_required
def home(request):
    return render(request, 'home.html')
