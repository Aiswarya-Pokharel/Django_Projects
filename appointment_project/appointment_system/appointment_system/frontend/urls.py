from django.urls import path
from . import views


urlpatterns = [
   path('', views.index, name='index'),
   path('insert/', views.insert, name='insert'),
   path('delete/', views.delete_appointment, name='delete'),
   path('edit/', views.edit_appointment, name='edit'),
]
