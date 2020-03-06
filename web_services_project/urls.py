"""web_services_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('teacherapi.urls')),##points to the urls file in teacher api to tell it what to do next
    path('register',include('teacherapi.urls')),
    path('login',include('teacherapi.urls')),
    path('list',include('teacherapi.urls')),
    path('rate',include('teacherapi.urls')),
    path('average',include('teacherapi.urls')),
    path('view',include('teacherapi.urls')),
    path('logout',include('teacherapi.urls')),

]
