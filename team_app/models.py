from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Year_Book(models.Model):
    year_frame = models.CharField(max_length= 10, null= False, blank= False)
    current_year = models.BooleanField(default= False)
 
    def __str__(self):
        return f'{self.year_frame}' '::' f'{self.current_year}'

    class Meta:
        db_table = 'Year Book'
        verbose_name_plural = 'Year Book'
        ordering = ['-id']


class Committee(models.Model):
    year = models.ForeignKey(Year_Book, on_delete= models.SET_NULL, null= True, blank= True)
    profile_pic = models.ImageField(upload_to='images/committees/profile_pic/', null= False, blank= False)
    name = models.CharField(max_length= 150, null= False, blank= False)
    position = models.CharField(max_length= 150, null= False, blank= False)
    address = models.CharField(max_length= 200, null= False, blank= False)
    bio = HTMLField()
    member_id = models.IntegerField(null= False, blank= False)

    def __str__(self):
        return f'{self.name}:: {self.year}'
    
    class Meta:
        db_table = 'Committee'
        verbose_name_plural = 'Committee'
        ordering = ['-id']
        

class SubMenu(models.Model):
    year = models.ForeignKey(Year_Book, on_delete= models.SET_NULL, null= True, blank= True)
    submenu = models.CharField(max_length= 100, null= False, blank= False)

    def __self__(self):
        return self.submenu

    class Meta:
        db_table = 'Sub Menu'
        verbose_name_plural = 'Sub Menu'
        ordering = ['-id']



