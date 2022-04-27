from django import forms
from django.db import models
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model=Person
        fields=['lname','fname', 'image','location','phone_number','email','goal']