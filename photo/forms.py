from django.forms import ModelForm
from .models import Pic
from django import forms

INPUT_CLASSES='w-full py-4 px-6 rounded-xl border'
class PicForm(forms.ModelForm):
     class Meta:
        model=Pic
        fields=['category','name','description','image',]
        widgets={
             'category':forms.Select(attrs={
              'class':INPUT_CLASSES
       }),
       'name':forms.TextInput(attrs={
              'class':INPUT_CLASSES
       }),
       'description':forms.Textarea(attrs={
              'class':INPUT_CLASSES
       }),
       'image':forms.FileInput(attrs={
              'class':INPUT_CLASSES
       }),
        }