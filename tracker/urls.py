"""tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from track.views import *

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('dashboard/', dashboard),
    path('directory/', directory),
    path('employee/<int:ecode>/', employee_page),
    path('add/', add_employee),
    path('suggestions/', suggestions),
    path('suggest/', suggestion_form),
    path('sotw/', star_of_the_week),
    path('star/', sotw_form),
    path('remove/<int:ecode>/', remove),
    path('remove1/<str:subject>/', remove1),
    path('remove2/<str:who>/', remove2),
    path('signup/', signup),
    path('signin/', signin),
    path('', home),
    path('edit/<int:ecode>/', edit),

]
