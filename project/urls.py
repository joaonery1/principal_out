"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from app.views import home,form,create,view,edit,update,delete,createSerie,formSerie,viewSerie,deleteSerie,updateSerie,homeSerie,editSerie
urlpatterns = [
    path('', home,name='home'),
    path('form/', form),
    path('homeSerie',homeSerie,name='homeSerie'),
    path('formSerie/',formSerie,name='formSerie'),
    path('create/', create, name='create'),
    path('view/<int:pk>/', view, name='view'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('editSerie/<int:pk>/', editSerie, name='editSerie'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('createSerie/', createSerie, name='createSerie'),
    path('viewSerie/<int:pk>/', viewSerie, name='viewSerie'),
    path('updateSerie/<int:pk>/', updateSerie, name='updateSerie'),
    path('deleteSerie/<int:pk>/', deleteSerie, name='deleteSerie'),
    

    
]