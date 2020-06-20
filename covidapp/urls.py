from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index),
    path('dashboard/', views.dashboard),
    path('logout/', views.logout),
    path('joined/',views.join),
    path('check/',views.check),
    path('delete/',views.delete),
    path('adminpanel/',views.admin),
    path('Bangalore/',views.Bangalore),
    path('Chandigarh/', views.Chandigarh),
    path('Chennai/', views.Chennai),
    path('Delhi/', views.Delhi),
    path('Hyderabad/', views.Hyderabad),
    path('Indore/', views.Indore),
    path('Jaipur/', views.Jaipur),
    path('Mumbai/', views.Mumbai),
    path('Mysore/', views.Mysore),
    path('Pune/', views.Pune),
    path('Surat/', views.Surat),
    path('', include('django.contrib.auth.urls')),
    path('', include('social_django.urls')),
]