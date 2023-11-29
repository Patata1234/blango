from django.urls import path 
from .views import index, post_detail

urlpatterns = [
    path('', index),
    path('post/<slug>/', post_detail, name='blog-post-detail'),    
]