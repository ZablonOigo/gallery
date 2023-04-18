from django.forms import ModelForm
from .models import Pic

class PicForm(ModelForm):
     class Meta:
        model=Pic
        fields=['category','name','description','image','created_by']