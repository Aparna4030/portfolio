"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.first),
    path('indexx',views.indexx),
    path('portfo',views.portfo),
    path('portforeg',views.portforeg),
    path('portfologg',views.portfologg),
    path('logout',views.logout),
    path('adminlogin',views.adminlogin),
    path('userlogin',views.userlogin),
    path('personaldet',views.personaldet),
    path('persodet',views.persodet),
    path('educationdet',views.educationdet),
    path('edudet',views.edudet),
    path('skills',views.skills),
    path('ski',views.ski),
    path('achievements',views.achievements),
    path('achieve',views.achieve),
    path('experience',views.experience),
    path('exp',views.exp),
    path('references',views.references),
    path('ref',views.ref),
    path('pview',views.pview),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
