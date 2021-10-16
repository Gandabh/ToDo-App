from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import *
from django.forms.fields import CharField

class TaskForm(forms.ModelForm):
    title = CharField(widget=forms.TextInput(attrs={'autofocus': True,
                                                            'class': 'form-control',
                                                            'placeholder': 'Enter your task here'
                                                            }))
 
    
    class Meta:
        model=Task
        fields='__all__'
    

