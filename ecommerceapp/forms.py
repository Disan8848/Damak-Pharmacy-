from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, SetPasswordForm, PasswordResetForm
from django.contrib.auth.models import User
from .models import Prescribed_Medicine

class PrescribedForm(forms.ModelForm):
    class Meta:
        model = Prescribed_Medicine
        fields = ['product', 'photo']
        labels = {
            'product': 'Medicine',
            'photo': 'Select Image'
        }
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
