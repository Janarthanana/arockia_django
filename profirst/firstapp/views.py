from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.contrib import messages


def loginfirst(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username='username', password='password')
        if user is not None:
            auth.login(request.user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'loginfirst.html')


def register(request):
    if request.method == 'POST':
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        uname = request.POST['username']
        emailid = request.POST['email']
        ps = request.POST['password']
        ps1 = request.POST['password1']
        if ps == ps1:
            if User.objects.filter(username=uname).exists():
                messages.info(request, 'Usename Already Exists')
                return redirect('register')
            elif User.objects.filter(email=emailid).exists():
                messages.info(request, 'Email Already Exists')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    email=emailid, firstname=fname, lastname=lname, password=ps)
                user.save()
                messages.info(request, 'User Created')
                return redirect('loginfirst')
    else:
        return render(request, 'register.html')


def dashboard(request):
    return render(request, 'dash.html')
