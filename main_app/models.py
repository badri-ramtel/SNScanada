from django.db import models
from django.core.validators import FileExtensionValidator 
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
    title = models.CharField(max_length= 100, null= False, blank= False)
    name = models.CharField(max_length= 100, null= False, blank= False)
    image = models.ImageField(upload_to= 'images/president/', null= False, blank= False)
    p_message = models.TextField()

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'President'
        verbose_name_plural = 'President'

class PresidentMessage(models.Model):
    message = models.CharField(max_length= 100, null= False, blank= False)

    def __self__(self):
        return f'{self.message}'

    class Meta:
        db_table = 'President Message'
        verbose_name_plural = 'President Message'

class Subscribe(models.Model):
    email = models.EmailField(max_length= 254)

    def __str__(self):
        return f'{self.email}'

    class Meta:
        db_table = 'Subscriber'
        verbose_name_plural = 'Subscriber'
        ordering = ['-id']


class Advertise(models.Model):
    content = models.ImageField(upload_to= 'images/advertise/', null= False, blank= False)

    def __str__(self):
        return f'{self.content}'
    
    class Meta:
        db_table = 'Advertisement'
        verbose_name_plural = 'Advertisement'
        ordering = ['-id']