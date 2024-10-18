from django.urls import path
from .views import index,about,client,contact,products

urlpatterns = [
    path('',index, name = 'index'),
    path('about/', about, name='about'),
    path('client/', client, name='client'),
    path('contacts/',  contact, name='contact'),
    path('products/', products, name='products'),
]
