from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Options 
from .models import Blogs
from .models import New
from .forms import BlogsForm

# Create your views here.
def index(request):
    if request.method=="POST":
        form = BlogsForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BlogsForm()
    options= Options.objects.all() #list of objects
    return render(request,'index.html',{'options':options,'form':form}) #need to send a dictionary

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        repassword=request.POST['password2'] 
        
        if password==repassword:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already exists')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username already exists')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Incorrect password')
            return redirect('register')
    else:
        return render(request, 'register.html')
def login(request):
    if request.method=="POST":
        username= request.POST['username']
        password=request.POST['password']

        user= auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request,'Credentials did not match')
            return redirect('login')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

def counter(request):
    text=request.POST['text']
    word_count=len(text.split())
    return render(request,'counter.html',{'count':word_count})

def back(request):
    return redirect('index') 

def post(request,pk):
    return render(request,'post.html',{'pk':pk})

def go_to_read(request):
    return redirect('read')

def go_to_home(request):
    return redirect('index')

def blog(request,pk):
    blogs=Blogs.objects.get(id=pk)
    return render(request,'blogs.html',{'blogs':blogs})

def go_to_explore(request):
    return redirect('explore')

def explore(request):
    new=New.objects.all()
    return render(request,'explore.html',{'new':new}) 

def read(request):
    blogs=Blogs.objects.all()
    total=len(blogs)
    return render(request,'read.html',{'blogs':blogs,'total':total}) 
