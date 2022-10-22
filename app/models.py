from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Note(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
        
    
