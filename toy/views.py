from django.shortcuts import render, get_object_or_404

from .models import Toy

def detail(request, pk):
    toy = get_object_or_404(Toy, pk=pk)
    related_toys = Toy.objects.filter(category=toy.category, stock__gt=0).exclude(pk=pk)[0:3]
    
    return render(request, 'toy/detail.html', {
        'toy': toy,
        'related_toys': related_toys,
    })
