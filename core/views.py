from django.shortcuts import render, redirect
from random import sample
from django.http import JsonResponse

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
    category_id = request.session.get('selected_category', None)

    if 'selected_category' in request.session:
        del request.session['selected_category']

    if category_id:
        toys = Toy.objects.filter(category_id=category_id, stock__gt=0)
    else:
        toys = Toy.objects.filter(stock__gt=0)

    categories = Category.objects.all()
    return render(request, 'core/shop.html', {
        'categories': categories,
        'toys': toys,
        'selected_category': category_id,
    })

def get_toys_by_category(request):
    category_id = request.GET.get('category')
    toys = Toy.objects.filter(category_id=category_id, stock__gt=0) if category_id else Toy.objects.filter(stock__gt=0)
    return render(request, 'core/toy_list_partial.html', {'toys': toys})

def set_category_session(request, category_id):
    request.session['selected_category'] = category_id
    return redirect('core:shop')
