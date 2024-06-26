from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Laws(models.Model):
    f_name = models.CharField(max_length= 254, null= False, blank= False)
    c_date = models.DateField(auto_created= False)
    files = models.FileField(upload_to= 'files/laws/', max_length= 254)

    def __str__(self):
        return f'{self.f_name}' 

    class Meta:
        db_table = 'Laws and Convention'
        verbose_name_plural = 'Laws and Convention'

class References(models.Model):
    f_name = models.CharField(max_length= 254, null= False, blank= False)
    c_date = models.DateField(auto_created= False)
    files = models.FileField(upload_to= 'files/references/', max_length= 254)

    def __str__(self):
        return f'{self.f_name}'

    class Meta:
        db_table = 'Reference'
        verbose_name_plural = 'Reference'


class Appreciations(models.Model):
    f_name = models.CharField(max_length= 254, null= False, blank= False)
    c_date = models.DateField(auto_created= False)
    files = models.FileField(upload_to= 'files/appreciations/', max_length= 254)

    def __str__(self):
        return f'{self.f_name}'

    class Meta:
        db_table = 'Appreciation'
        verbose_name_plural = 'Appreciation'

class Registrations(models.Model):
    f_name = models.CharField(max_length= 254, null= False, blank= False)
    c_date = models.DateField(auto_created= False)
    files = models.FileField(upload_to= 'files/registrations/', max_length= 254)

    def __str__(self):
        return f'{self.f_name}'

    class Meta:
        db_table = 'Registration'
        verbose_name_plural = 'Registration'

CONDITION = {
    'C' : 'Confirmed',
    'U' : 'Unconfirm'
}

class Program_Registrations(models.Model):
    date = models.DateTimeField(auto_now_add= True)
    participant_full_name = models.CharField(max_length= 200, null= False, blank= False)
    age = models.IntegerField(null= False, blank= False)
    address = models.CharField(max_length= 200, null= False, blank= False)
    city = models.CharField(max_length= 400, null= False, blank= False)
    province = models.CharField(max_length= 400, null= False, blank= False)
    postal_code = models.IntegerField(null= True, blank= True)
    your_contact = PhoneNumberField(max_length= 13, null= False, blank= False, help_text= 'your contact number')
    your_email = models.EmailField(max_length= 254, null= False, blank= False)
    parents_full_name = models.CharField(max_length= 200, null= False, blank= False)
    parents_contact = PhoneNumberField(max_length= 13, null= False, blank= False, help_text= 'your contact number')
    parents_email = models.EmailField(max_length= 254, null= False, blank= False)
    categories = (
        ("SUMMER", 'summer'), 
        ("WINTER", 'winter'),
    )
    program = models.CharField(max_length= 12, choices= categories)
    screenshot = models.ImageField(upload_to= 'images/payments/program_registration/', null= False, blank= False)
    status = models.CharField(max_length= 1, choices= CONDITION, default= 'U')

    def __str__(self):
        return f'{self.participant_full_name}- ({self.date})'
    
    class Meta:
        db_table = 'Program Registration'
        verbose_name_plural = 'Program Registration'

