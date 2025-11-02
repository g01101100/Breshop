from django.db import models

class Adress(models.Model):
    CEP = models.CharField(max_length = 8)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    street = models.CharField(max_length=50)
    number = models.IntegerField()
	
    def __str__(self) -> str:
        return self.CEP
    
class Contact(models.Model):
    email = models.EmailField()
    phone = models.IntegerField()
    instagram = models.CharField(null=True, max_length=30)

    def __str__(self) -> str:
        return self.email


# Create your models here.
