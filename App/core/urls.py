# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),             # URL pattern for home.html (root URL)
    path('home.html', views.home, name='home'),     # Additional URL pattern for home.html
    path('hone.html', views.hone, name='hone'),     # URL pattern for hone.html
]
