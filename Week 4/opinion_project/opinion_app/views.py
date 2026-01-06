from django.shortcuts import render, redirect
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')


def add_opinion(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        election_area = request.POST.get('election_area')
        party = request.POST.get('party')

        
        return render(request, 'thank_you.html')

    return render(request, 'add_opinion.html')


def thank_you(request):
    return render(request, 'thank_you.html')


def all_opinions(request):
    return render(request, 'all_opinions.html')
