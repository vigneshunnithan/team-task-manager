from django.shortcuts import render, redirect
from .forms import TaskForm


def create_task(request):

    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.user.role != 'ADMIN':
     return redirect('dashboard')

    if request.method == 'POST':

        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    else:
        form = TaskForm()

    return render(request, 'create_task.html', {'form': form})