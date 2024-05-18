from django.db import models

from about_app.models import About
# Create your models here.

class Slider(models.Model):
    picture = models.ImageField(upload_to= 'images/slider/', null= False, blank= False)
    title = models.CharField(max_length= 100, null= False, blank= False)
    sub_title = models.CharField(max_length= 254, null= False, blank= False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Slider'
        verbose_name_plural = 'Slider'
        ordering = ['-id']


class President(models.Model):
    name = models.CharField(max_length= 100, null= False, blank= False)
    image = models.ImageField(upload_to= 'images/president/', null= False, blank= False)
    p_message = models.TextField()

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'President'
        verbose_name_plural = 'President'

class Subscribe(models.Model):
    email = models.EmailField(max_length= 254)

    def __self__(self):
        return self.email

    class Meta:
        db_table = 'Subscribe'
        verbose_name_plural = 'Subscribe'
        ordering = ['-id']