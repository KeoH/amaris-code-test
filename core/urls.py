from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from .views import IndexView
from employees.views import ProfileView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employees/', include('employees.urls')),
    path('accounts/login/', auth_views.login, {'template_name' : 'auth/login.html'}, name='login'),
    path('accounts/logout/', auth_views.logout, {'template_name' : 'auth/logout.html'}, name='logout'),
    path('accounts/profile/', ProfileView.as_view(), {'page' : 'profile'}, name='profile'),
    path('', IndexView.as_view(), {'page' : 'index'}, name="index")
]
