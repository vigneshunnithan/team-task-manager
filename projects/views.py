from django.shortcuts import render, redirect
from .forms import ProjectForm


def create_project(request):

    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.user.role != 'ADMIN':
     return redirect('dashboard')

    if request.method == 'POST':

        form = ProjectForm(request.POST)

        if form.is_valid():

            project = form.save(commit=False)
            project.created_by = request.user
            project.save()

            form.save_m2m()

            return redirect('dashboard')

    else:
        form = ProjectForm()

    return render(request, 'create_project.html', {'form': form})