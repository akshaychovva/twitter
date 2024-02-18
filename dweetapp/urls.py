from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_dweet, name='show_dweet'),
    path('<int:pk>/', views.update_dweet, name='update_dweet'),
    path('like/<int:pk>', views.like, name='like'),
]