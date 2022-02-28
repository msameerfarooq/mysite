"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from myapp import views
from .views import BookingDetailsSet,RoomsSet,HotelSet,CountrySet

router = routers.DefaultRouter()
router.register('Booking', BookingDetailsSet, basename='Booking')
router.register('Room',RoomsSet, basename='Room')
router.register('Hotel',HotelSet,basename='Hotel')
router.register('Country', CountrySet,basename='Country')

urlpatterns = [
    path('',include(router.urls)),
    path('admin/', admin.site.urls),
]

"""urlpatterns = [
    path('home/',views.home,name='dashboard'),
    path('book/',views.home,name='book'),
    path('unbook/',views.home,name='home'),
    path('admin/', admin.site.urls),
]
"""