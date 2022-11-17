from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
        path('',views.index,name='index'),
        path('base',views.base,name='base'),
        path('gallery',views.gallery,name='gallery'),
        path('updates',views.updates,name='updates'),
        path('contact',views.contact,name='contact'),
        path('contentpage',views.contentpage,name='updates-contentpage'),

]