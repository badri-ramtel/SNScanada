from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class About(models.Model):
    about_content = HTMLField(null= False, blank= False)

    def __self__(self):
        return self.about_content
    
    class Meta:
        db_table = 'About SNS'
        verbose_name_plural = 'About SNS'


class Vision(models.Model):
    vision_content = HTMLField(null= False, blank= False)

    def __self__(self):
        return self.vision_content
    
    class Meta:
        db_table = 'Vision'
        verbose_name_plural = 'Vision'


class Term(models.Model):
    term_content = HTMLField(null= False, blank= False)

    def __self__(self):
        return f'{self.term_content}'
    
    class Meta:
        db_table = 'Terms and Condition'
        verbose_name_plural = 'Terms and Condition'

class News(models.Model):
    title = models.CharField(max_length= 200, null= False, blank= False)
    sub_title = models.CharField(max_length= 200, null= False, blank= False)
    date = models.DateField(auto_created= False, null= False)
    news_image = models.ImageField(upload_to= 'images/news/', null= True, blank= True)
    brief = HTMLField(null= False, blank= False)
    hide = models.BooleanField()

    def __str__(self):
        return f"{self.title}"

    class Meta:
        db_table = 'News'
        verbose_name_plural = 'News'
        ordering = ['-id']
