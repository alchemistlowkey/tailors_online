from django.db import models
from django.contrib.auth.models import User


class UserMeasurement(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    height = models.FloatField()
    chest_size = models.FloatField()
    waist_size = models.FloatField()
    # Add other measurement fields as needed
    def __str__(self):
        return f'{self.user.username} UserMeasurement'
    