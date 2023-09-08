from django.shortcuts import render

from toy.models import Category, Toy


def index(request):
    toys = Toy.objects.filter(stock__gt=0).order_by('-date_time_created')[0:3]
    categories = Category.objects.all()
    
    return render(request, 'core/index.html', {
        'categories': categories,
        'toys': toys,
    })

def contact(request):
    return render(request, 'core/contact.html')