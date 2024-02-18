from django.forms import ModelForm
from .models import Dweet

class DweetForm(ModelForm):
    class Meta:
        model = Dweet
        fields = ['body']