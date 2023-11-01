from django.shortcuts import render
from django.shortcuts import redirect
from .forms import ProductForm

# Create your views here.

def index(req):
    if req.method == 'POST':
        form = ProductForm(req.POST)
        form.save()
        return redirect('/display')
    form = ProductForm()
    return render(req, 'index.html',{'form':form})

def create(req):
    
    return render(req,'create.html')
def display(req):
    return render(req,'display.html')
def update(req):
    return render(req,'update.html')
def delete(req):
    return redirect('/display')