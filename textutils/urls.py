"""textutils URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from . import views    # to connect views to this page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  #'' => in homepage // views.index =>it will go to view named file where he will rin index function 
                                           #// name='index' => given a name to acces this easily as path name may be very big and comple like 'nudcbdvwvduwvcyugndoudwhmougducygbdwycgdwuchduonncg8ytdfcdnc dgc'
                                           # it will difficult to acces through path but easy to acces through name
    path('analyze', views.analyze, name='analyze'),
    path('about', views.about, name='about')

]
