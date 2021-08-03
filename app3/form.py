from django.db.models.base import Model
from django.forms import fields, models
from django import forms
from .models import blog,page,feedback

class blogpage(forms.ModelForm):
    class Meta:
        model = blog
        fields = ['title','slug','author','status','image','image1']

class apppagefile(forms.ModelForm):
    class Meta:
        model = page
        fields = ['Question','Answer']

class frompage(forms.ModelForm):
    class Meta:
        model = feedback
        fields = ['image','description']