from django import forms
from django.forms import ModelForm
from .models import member

class MemberForm(ModelForm):
    class Meta: 
        model = member # Updated to use correct class name

        fields = ('Name', 'Category', 'Amount' )

        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'Category': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category'}),
            'Amount': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Amount'}),
            
        }