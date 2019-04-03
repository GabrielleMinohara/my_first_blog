<<<<<<< HEAD
from django.urls import path
=======
from django.urls import path 
>>>>>>> parent of 14887a1... Versão final
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
<<<<<<< HEAD
=======
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
>>>>>>> parent of 14887a1... Versão final
]


