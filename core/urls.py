from django.contrib import admin
from django.urls import path
from projects.views import create_project
from tasks.views import create_task
from accounts.views import (
    home,
    signup_view,
    login_view,
    logout_view,
    dashboard
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),

    path('signup/', signup_view, name='signup'),

    path('login/', login_view, name='login'),

    path('logout/', logout_view, name='logout'),

    path('dashboard/', dashboard, name='dashboard'),

    path('projects/create/', create_project, name='create_project'),

    path('tasks/create/', create_task, name='create_task'),
]