from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.my_friends, name='profiles' ),
    path('<int:pk>',views.add_friend, name='add_friend' ),
]