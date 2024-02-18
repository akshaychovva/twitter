from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile


class CustomUserCreation(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'email']


class LoginForm():
    class Meta:
        model = UserProfile
        fields = ['email', 'password']
