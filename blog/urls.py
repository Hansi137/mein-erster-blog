from django.urls import path
from . import views
#Hier importieren wir die Django-Funktion path und alle unsere views aus unserer blog-Applikation. (Wir haben noch keine, aber dazu kommen wir gleich!)

#Jetzt können wir unser erstes URL-Muster hinzufügen:

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
