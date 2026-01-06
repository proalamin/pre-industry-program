from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def add_opinion(request):
    return render(request, 'add_opinion.html')


def all_opinions(request):
    return render(request, 'all_opinions.html')
