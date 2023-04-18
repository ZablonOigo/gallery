from django.shortcuts import render,redirect,get_object_or_404

from .models import *
from .forms import *

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


def create_photo(request):
    if request.method == 'GET':
        context={'form':PicForm()}
        return render(request,'photo/create.html',context)
    
    elif request.method =='POST':
        form=PicForm(request.POST,request.FILES)
        if form.is_valid():
            user=form.save(commit=False)
            user.created_by=request.user
            user.save()
            return redirect('detail', id=user.id)
        else:
            return render(request,'photo/create.html', {'form':form})
        

def update_photo(request,id):
    pic=get_object_or_404(Pic, id=id)
    if request.method == 'GET':
        context={'form':PicForm(instance=pic),'id':id}
        return render(request,'photo/create.html',context)  

    elif request.method =='POST':
        form=PicForm(request.POST, instance=pic)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request, 'photo/create.html', {'form':form})         
        





def delete_photo(request, id):
    pic=get_object_or_404(Pic, id=id) 
    context={'pic':pic}
    if request.method =='GET':
        return render(request,'photo/delete_pic.html', context)

    elif request.method =="POST":
        pic.delete()
        return redirect('index')       