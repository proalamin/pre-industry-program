from django.shortcuts import render, redirect
from .models import Opinion

def home(request):
    opinions = Opinion.objects.all().order_by('-id')[:3]
    return render(request, 'home.html', {'opinions': opinions})


def add_opinion(request):
    if request.method == 'POST':
        Opinion.objects.create(
            name=request.POST.get('name'),
            phone=request.POST.get('phone'),
            election_area=request.POST.get('election_area'),
            party=request.POST.get('party'),
        )
        return redirect('thank_you')

    return render(request, 'add_opinion.html')


def thank_you(request):
    return render(request, 'thank_you.html')


def all_opinions(request):
    opinions = Opinion.objects.all().order_by('-id')
    return render(request, 'all_opinions.html', {'opinions': opinions})
