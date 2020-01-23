from django.urls import path
from . import views
#Hier importieren wir die Django-Funktion path und alle unsere views aus unserer blog-Applikation. (Wir haben noch keine, aber dazu kommen wir gleich!)

#Jetzt können wir unser erstes URL-Muster hinzufügen:

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
