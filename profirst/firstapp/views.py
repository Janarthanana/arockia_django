from django.shortcuts import render


def loginfirst(request):
    return render(request, 'loginfirst.html')

def register(request):
	return render(request, 'register.html')