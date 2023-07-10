from django.urls import path
from . import views

urlpatterns=[
    path('',views.registerpage,name=('Django_Project'))
]