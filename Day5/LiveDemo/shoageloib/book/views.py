from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
def List(req):
    return HttpResponse('<h1>Book List</h1>')
def Add(req):
    return HttpResponse('<h1>Book Add</h1>')