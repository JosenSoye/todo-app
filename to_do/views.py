from django.shortcuts import render,redirect

# Create your views here.
from .form import todoform
from . models import Todo



# Create your views here.
def sub(req):
    return render(req,'sub.html')

def show(req):
    if req.method == 'POST':
        form=todoform(req.POST)
        if form.is_valid():
            form.save()
            return redirect(table)
    else:
        form=todoform()
    return render(req,'show.html',{'form':form}) 

def table(req):
    todo1=Todo.objects.all()
    return render(req,'table.html',{'d':todo1})
def view(req,id):
    todo2=Todo.objects.get(id=id)
    return render(req,'view.html',{'data':todo2})

def edit(req,id):
    todo3=Todo.objects.get(id=id)
    if req.method=='POST':
        form=todoform(req.POST,instance=todo3)
        if form.is_valid():
            form.save()
            return redirect(table)
    else:
        form=todoform(instance=todo3)
    return render(req,'edit.html',{'form':form})
    
def delete(req,id):
    todo4=Todo.objects.get(id=id)
    todo4.delete()