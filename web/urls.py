from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
        path('',views.index,name='index'),
        path('base',views.base,name='base'),
        path('gallery',views.gallery,name='gallery'),
        path('updates',views.updates,name='updates'),
        # path('project',views.project,name='project'),
        path('contact',views.contact,name='contact'),
        path('contentpage/<id>',views.contentpage,name='updates-contentpage'),
        path('content/<id>',views.content,name='content'),
]