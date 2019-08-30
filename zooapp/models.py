from django.db import models
from django.db import models
from random import *
# Create your models here.
class Registration(models.Model):
    Type = (
        ('male','male'),
        ('female','female'),
        ('other','other')
    )
    Choices = (
        ('local','local'),
        ('nonlocal','nonlocal')
    )
    p = ''
    for i in range(0,4):
        p = p+str(randint(0,9))
    Employ_id = models.PositiveIntegerField(default = p)
    Employ_name = models.CharField(max_length = 50)    
    email = models.EmailField()
    password = models.CharField(max_length=30)
    age = models.CharField(max_length=3)
    gender = models.CharField(max_length=30,choices=Type)
    contact_number = models.CharField(max_length=30)
    address = models.TextField(max_length=300)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    pincode = models.CharField(max_length=30)
    def __str__(self):
        return self.Employ_name

class Booking(models.Model):
    Type = (
        ('male','male'),
        ('female','female'),
        ('other','other')
    )  
    
    TIMING= (
        ('09:30 am to 10:30 am','09:30 am to 10:30 am'),
        ('11:00 am to 12:00 pm','11:00 am to 12:00 pm'),
        ('12:30 pm to 01:30 pm','12:30 pm to 01:30 pm'),
        ('02:30 pm to 03:30 pm','02:30 pm to 03:30 pm'),
        ('04:00 pm to 05:30 pm','04:00 pm to 05:30 pm'),
    )    
    Date = models.DateField(help_text='mm/dd/yyyy')
    Vistorname = models.CharField(max_length =50)
    age = models.CharField(max_length =50)
    gender = models.CharField(max_length=30,choices=Type)
    TimeSlot = models.CharField(max_length = 50,choices = TIMING)
    Vehicle_No = models.CharField(max_length = 50)
    email = models.EmailField()
    phone_no = models.CharField(max_length=50)
    ticketprice = models.IntegerField()
    def __str__(self):
        return self.Vistorname


