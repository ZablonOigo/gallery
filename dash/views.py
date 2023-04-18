from django.shortcuts import render
from photo.models import *
def index(request):
    categories=Category.objects.all()
    pics=Pic.objects.filter(created_by=request.user)
    return render(request, 'dash/index.html',{'pics':pics,'categories':categories})
