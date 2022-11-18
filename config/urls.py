"""config URL Configuration

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
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from mainapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mahsulotlar/', MahsulotlarAPIView.as_view()),
    path('mahsulot/<int:pk>/', MahsulotAPIView.as_view()),
    path('mijozlar/', MijozlarAPIView.as_view()),
    path('mijoz/<int:pk>/', MijozlarAPIView.as_view()),
    path('sotuvchilar/', SotuvchilarAPIView.as_view()),
    path('statistikalar/', StatistikalarAPIView.as_view()),
    path('tokenlar/', TokenlarAPIView.as_view()),
    path('get_token/', obtain_auth_token),
    path('userlar/', UserlarAPIView.as_view()),
]
