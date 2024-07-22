from django.db import models
import uuid

class Asset(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    asset_id = models.CharField(max_length=100, unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.asset_id:
            self.asset_id = str(uuid.uuid4()).replace('-', '')[:12]  # Generate a unique asset ID
        super(Asset, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Maintenance(models.Model):
    CATEGORY_CHOICES = [
        ('Laptops', 'Laptops'),
        ('Desktops', 'Desktops'),
        ('Extensions', 'Extensions'),
        ('Banners', 'Banners'),
        ('Screens', 'Screens')
    ]
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    maintenance_date = models.DateField()
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    comments = models.TextField()

    def __str__(self):
        return f'Maintenance for {self.asset.name} on {self.maintenance_date}'

class TrackingMovement(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    previous_location = models.CharField(max_length=255, blank=True, null=True)
    new_location = models.CharField(max_length=255)
    tracking_date = models.DateField()
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.asset} moved from {self.previous_location} to {self.new_location} on {self.tracking_date}'

