from django.db import models

class ContactFormEntry(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    comments = models.TextField()

    def __str__(self):
        return f"Contact form from {self.name} ({self.email})"
