from django.shortcuts import render
from . import ml

def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def result(request):
    user_input = request.GET['user_input']
    user_input = ml.multi(user_input)
    return render(request, 'result.html', {'home_input':user_input})
