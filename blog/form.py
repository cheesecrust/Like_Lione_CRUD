from importlib.resources import contents
from pyexpat import model
from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'contents', 'image']
