from django import forms
from .models import Registration
 
 
class RegistrationModel(forms.ModelForm):
 
    class Meta:
        model = Registration
        fields = [
            'username',
            'password',
        ]