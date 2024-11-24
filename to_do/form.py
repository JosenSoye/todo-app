from django import forms
from django.forms import ValidationError
from .models import Todo

class todoform(forms.ModelForm):
    name = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'l1','placeholder':'Enter todo list'}))
    des = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'l2','placeholder':'Enter todo list description'}))
    class Meta:
        model = Todo
        fields = ['name','des']
