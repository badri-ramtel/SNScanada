from django.db import models
from datetime import datetime

# Create your models here.
class Year_Book(models.Model):
    year_frame = models.CharField(max_length= 10, null= False, blank= False)
    current_year = models.BooleanField(default= False)

    def __str__(self):
        return f'{self.year_frame}' '::' f'{self.current_year}'

    class Meta:
        db_table = 'Year Book'
        verbose_name_plural = 'Year Book'


class Committee(models.Model):
    year = models.ForeignKey(Year_Book, on_delete= models.SET_NULL, null= True, blank= True)
    profile_pic = models.ImageField(upload_to='upload/', null= False)
    name = models.CharField(max_length= 150, null= False, blank= False)
    position = models.CharField(max_length= 150, null= False, blank= False)
    address = models.CharField(max_length= 200, null= False, blank= False)
    education = models.CharField(max_length= 100, null= False, blank= False)
    profession = models.CharField(max_length= 100, null= False, blank= False)
    email = models.EmailField()

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Committee'
        verbose_name_plural = 'Committee'
        ordering = ['-id']
        


