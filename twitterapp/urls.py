from django.urls import path
from . import views


app_name = 'user_name'

urlpatterns = [
    path('', views.show_users, name='show_users'),
    path('<int:pk>', views.show_user, name='userprofile'),
    path('register', views.register_user, name='register_user'),
    path('login_or_reg', views.login_or_reg, name='login_or_reg'),
    path('login', views.login_user, name='login_user'),
    path('logout', views.logout_user, name='logout_user'),
    path('friend_requests', views.friend_requests, name='friend_requests'),
    path('friend_requests/<int:pk>', views.friend_requests, name='friend_requests'),
]