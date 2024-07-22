from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class CreateEvent(models.Model):
    event_name = models.CharField(max_length= 60, null= False, blank= False)
    event_created_date = models.DateField(auto_created= False, null= True)

    def __str__(self):
        return self.event_name

    class Meta:
        db_table = 'Create New Event'
        verbose_name_plural = 'Create New Event'
        ordering = ['-id']


class Event(models.Model):
    created_events = models.ForeignKey(CreateEvent, on_delete=models.SET_NULL, null= True, blank= True)
    title = models.CharField(max_length= 200, null= False, blank= False)
    sub_title = models.CharField(max_length= 200, null= False, blank= False)
    date = models.DateField(auto_created= False, null= False)
    event_image = models.ImageField(upload_to= 'images/event/', null= True, blank= True)
    brief = HTMLField(null= False, blank= False)
    hide = models.BooleanField()

    def __str__(self):
        return f"{self.title}"

    class Meta:
        db_table = 'Event'
        verbose_name_plural = 'Event'
        ordering = ['-id']