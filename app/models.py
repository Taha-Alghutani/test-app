from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='items/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
