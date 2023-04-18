from django.shortcuts import render,redirect,get_object_or_404

from .models import *

def index(request):
    categories=Category.objects.all()
    pics=Pic.objects.all()
    context={'categories':categories,'pics':pics}
    return render(request, 'photo/index.html', context )

def view_photo(request, id):
    pics=get_object_or_404(Pic,id=id)
    related_items=Pic.objects.filter(category=pics.category).exclude(id=id)[0:3]
    context={'pics':pics,
             'related_items':related_items}
    return render(request, 'photo/view.html', context)