from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignupForm
from tasks.models import Task
from datetime import date


def home(request):
    return render(request, 'home.html')

def dashboard(request):

    if not request.user.is_authenticated:
        return redirect('login')

    tasks = Task.objects.filter(assigned_to=request.user)

    completed_tasks = tasks.filter(status='DONE').count()
    pending_tasks = tasks.exclude(status='DONE').count()

    context = {
        'tasks': tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
        'today': date.today(),
    }

    return render(request, 'dashboard.html', context)


def signup_view(request):

    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/dashboard/')

    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})


def login_view(request):

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/dashboard/')

    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')