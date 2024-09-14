from django.shortcuts import render

# Create your views here.
def signupaction(request):
    if request.metod == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        data=user.objects.create_user(username=username,email=email,password=password)
    return None