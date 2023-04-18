from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=120)

    class Meta:
        ordering=['-name']
        verbose_name_plural='Categories'

    def __str__(self):
        return self.name    
    

class Pic(models.Model):
    category=models.ForeignKey(Category, related_name='pics', on_delete=models.SET_NULL, null=True)
    name=models.CharField(max_length=50)
    description=models.TextField(blank=True, null=True)
    image=models.ImageField(upload_to='image')
    created_by=models.ForeignKey(User,related_name='pics',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return  self.name