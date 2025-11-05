from django.db import models

class Adress(models.Model):
    CEP = models.CharField(max_length=8)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    street = models.CharField(max_length=50)
    number = models.IntegerField()

    def __str__(self) -> str:
        return f'state: {self.state} | city: {self.city}'
	

class Brecho(models.Model):
    name = models.CharField(max_length=50)
    adress = models.OneToOneField(Adress, null=True, on_delete = models.SET_NULL)

    def __str__(self) -> str:
        return self.name


class Contact(models.Model):
    email = models.EmailField(primary_key=True)
    phone = models.CharField(null=True, max_length=30)
    instagram = models.CharField(null=True, max_length=30)
    brecho = models.ForeignKey(Brecho, on_delete = models.CASCADE)

    def __str__(self) -> str:
            return self.email


class Tag(models.Model):
    name = models.CharField(primary_key=True)
    
    def __str__(self) -> str:
        return self.name


class Produto(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brecho = models.ForeignKey(Brecho, on_delete = models.CASCADE) 
    tags = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return self.name


class User(models.Model):
    name = models.CharField(max_length=50)
    adress = models.ForeignKey(Adress, null=True, on_delete = models.SET_NULL)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.name


# Create your models here.