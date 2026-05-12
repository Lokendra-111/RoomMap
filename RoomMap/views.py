from django.shortcuts import render, redirect
from .models import Signup

def home(request):

    if request.method == "POST":

        # SIGNUP
        if 'signup_username' in request.POST:

            fullname = request.POST.get('fullname')
            username = request.POST.get('signup_username')
            email = request.POST.get('email')
            password = request.POST.get('signup_password')

            data = Signup(
                fullname=fullname,
                username=username,
                email=email,
                password=password
            )

            data.save()

            return redirect('/')

        # LOGIN
        elif 'login_username' in request.POST:

            username = request.POST.get('login_username')
            password = request.POST.get('login_password')

            user = Signup.objects.filter(
                username=username,
                password=password
            )

            if user.exists():
                return redirect('/dashboard/')

    return render(request, 'index.html')


def dashboard(request):
    return render(request, 'dashboard.html')