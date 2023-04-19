from django.shortcuts import render,redirect,get_object_or_404
from django.db.models import Q
from .models import *
from django.contrib.auth.decorators import login_required
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

@login_required
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
            return redirect('photo:detail', id=user.id)
        else:
            return render(request,'photo/create.html', {'form':form})
        
@login_required
def update_photo(request,id):
    query=Pic.objects.filter(created_by=request.user)
    pic=get_object_or_404(query, id=id)
    if request.method == 'GET':
        context={'form':PicForm(instance=pic),'id':id}
        return render(request,'photo/create.html',context)  

    elif request.method =='POST':
        form=PicForm(request.POST, instance=pic)
        if form.is_valid():
            form.save()
            return redirect('photo:index')
        else:
            return render(request, 'photo/create.html', {'form':form})         
        




@login_required
def delete_photo(request, id):
    query=Pic.objects.filter(created_by=request.user)
    pic=get_object_or_404(query, id=id) 
    context={'pic':pic}
    if request.method =='GET':
        return render(request,'photo/delete_pic.html', context)

    elif request.method =="POST":
        pic.delete()
        return redirect('photo:index')       
    



  
def  search_pic(request):
    query=request.GET.get('query','')
    category_id=request.GET.get('category',0)
    categories=Category.objects.all()
    pics=Pic.objects.all()
    if category_id:
        pics=pics.filter(category_id=category_id)
    if query:
        pics=pics.filter(Q(name__icontains=query)|Q(description__icontains=query)) 
    return render(request,'photo/pics.html',{
        'query':query,
        'category_id':int(category_id),
        'pics':pics,
        'categories':categories,
    })        