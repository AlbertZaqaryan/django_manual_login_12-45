from django.db import models

# Create your models here.

class MyUser(models.Model):

    user_name = models.CharField('User name', max_length=60)
    user_password = models.CharField('User password', max_length=16)

    def __str__(self):
        return self.user_name
    
    