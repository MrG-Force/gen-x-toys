from django.shortcuts import render, redirect
from random import sample

from toy.models import Category, Toy

from .forms import SignupForm


def index(request):
    toys = Toy.objects.filter(stock__gt=0)
    count = toys.count()
    random_toys_indices = sample(range(count), min(3, count))
    toys = [toys[i] for i in random_toys_indices]

    categories = Category.objects.all()
    
    return render(request, 'core/index.html', {
        'categories': categories,
        'toys': toys,
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    form = SignupForm()
    suggested_username = form.suggested_username
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/login/')

    return render(request, 'core/signup.html', {
        'form': form,
        'suggested_username': suggested_username,
    })

def logout(request):
    logout(request)
    return redirect(request, 'core/index.html')

def shop(request):
    toys = Toy.objects.filter(stock__gt=0)
    categories = Category.objects.all()
    return render(request, 'core/shop.html', {
        'categories': categories,
        'toys': toys,
    })