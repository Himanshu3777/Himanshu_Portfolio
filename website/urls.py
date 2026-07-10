# website/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('messages/', views.messages_view, name='messages'),
    path('submit-form/', views.submit_form, name='submit_form'),

]
