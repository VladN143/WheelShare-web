from django.db import models

from django.contrib.auth.models import AbstractUser

# Tipuri de cont
ACCOUNT_TYPES = [
    ('renter', 'Închiriază'),
    ('owner', 'Proprietar'),
]

class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=50)
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPES)

    def __str__(self):
        return self.username

class Car(models.Model):
    model = models.CharField(max_length=100)
    an_fabricatie = models.IntegerField()
    pret = models.DecimalField(max_digits=10, decimal_places=2)
    detalii = models.TextField()
    imagine = models.ImageField(upload_to='masini/', null=True, blank=True)
    dealer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'account_type': 'owner'})

    def __str__(self):
        return f"{self.model} ({self.year})"

class Review(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'account_type': 'renter'})
    rating = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f"Recenzie de la {self.user.username} pentru {self.car.model}"
    

from django.contrib.auth import get_user_model
User = get_user_model()
    
class CarRented(models.Model):
    masina = models.ForeignKey(Car, on_delete=models.CASCADE)
    utilizator = models.ForeignKey(User, on_delete=models.CASCADE)
    data_inchiriere = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.utilizator.username} a închiriat {self.masina.model}"
    

