from django.urls import path
from . import views


urlpatterns = [
    path('<int:pk>', views.comment, name='comment'),
    path('update_comment/<int:pk>', views.update_comment, name='update_comment'),
    path('like_comment/<int:pk>', views.like_comment, name='like_comment'),
]