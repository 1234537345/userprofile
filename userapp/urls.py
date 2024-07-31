# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.createuserProfile, name='create'),
    path('listdetails/', views.listdetails, name='details'),
    path('updatedetails/<int:p_id>/', views.updatedetails, name='update'),
    path('deletedetails/<int:p_id>/', views.deletedetails, name='delete'),
    path('index/', views.index, name='index')
]

