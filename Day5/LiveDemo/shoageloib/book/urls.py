from django.urls import path
from .views import *
urlpatterns=[
    path('',List,name='Book_List'),
    path('Add',Add,name='Book_Add'),
]