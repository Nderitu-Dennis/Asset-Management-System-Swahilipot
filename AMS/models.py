# AMS/models.py

from django.db import models

class MaintenanceRequest(models.Model):
    CATEGORY_CHOICES = [
        ('Laptops', 'Laptops'),
        ('Desktops', 'Desktops'),
        ('Extensions', 'Extensions'),
        ('Banners', 'Banners'),
        ('Screens', 'Screens'),
    ]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    asset_id = models.CharField(max_length=100)
    comments = models.TextField()

    def __str__(self):
        return f"{self.category} - {self.asset_id}"
