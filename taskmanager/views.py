#views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Task, LogEntry, CustomUser
from .forms import SignInForm,SignUpForm

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Extract username from the form
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            # Authenticate using the Customer Model
            user = authenticate(request, username=username, password=password, model=CustomUser)
            #Check if authentication was successful
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = SignUpForm()
    return render(request, "taskmanager/signup.html", {"form": form})

def signin(request):
    if request.method == "POST":
        form = SignInForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect("index")
    else:
        form = SignInForm()
    return render(request, "taskmanager/signin.html", {"form": form})

@login_required
def home(request):
    #Retreive tasks for the logged-in user
    tasks = Task.objects.filter(log_entry_set__user=request.user)
    context = {
        "tasks": tasks,
    }
    return render(request, "taskmanager/index.html", context)


