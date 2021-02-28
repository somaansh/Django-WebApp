from django.db import models

# Create your models here.

class Contact(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    query = models.TextField()
    date = models.DateField()
    def __str__(self):
        return self.fname
    
class Registration(models.Model):
    fullname = models.CharField(max_length=100)
    photograph = models.ImageField(upload_to='image/')
    email_id = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=100)
    pswd = models.CharField(max_length=100)
    Confirm_pswd = models.CharField(max_length=100)
    city_live = models.CharField(max_length=100)
    state_live = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    id_card = models.ImageField(upload_to='image/')
    date = models.DateField()
    def __str__(self):
        return self.fullname

    
    
    
