from django.urls import path

from .views import  image_create , image_detail

appname = 'images'

urlpatterns = [
    path('create/', image_create , name='create'),
    path('detail/<int:id>/<slug:slug>/', image_detail, name='detail'),
    
]
