from django.db import models

# Create your models here.
class patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    medical_history = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name