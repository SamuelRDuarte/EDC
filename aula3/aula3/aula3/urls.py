"""aula3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('curso/', views.curso, name='curso'),
    path('cursoDepart/', views.cursospordepart, name="cursoDepart"),
    path('cursoGrau/', views.cursosporgrau, name="cursoGrau"),
    path('cursoAreaCientifica/', views.cursosporareacientifica, name="cursoAreaCientifica"),
    path('cursoLocal/', views.cursosporlocal, name="cursoLocal"),
    path('departamentos/', views.departamentos, name="departamentos"),
    path('areascientificas/', views.areascientificas, name="areascientificas"),
    path('locais/', views.locais, name="locais"),
    path('cursoDetails/', views.cursodetails, name='cursoDetails'),
]
