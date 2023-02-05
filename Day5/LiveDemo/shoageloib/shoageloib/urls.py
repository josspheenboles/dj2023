"""shoageloib URL Configuration

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
from django.urls import path,include
#import view
from catagory import views
from book import views as bookview
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Catg/List',views.List,name='Catagory_List'),
    path('Catg/Add',views.Add,name='Catagory_Add'),
    path('Catg/Update/<int:catgid>',views.Update,name='Catagory_Update'),
    path('Book/',include('book.urls'))

]