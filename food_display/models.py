from django.db import models

# Create model called Food to store the food details.
class Food(models.Model):
    Name = models.CharField(max_length=50)
    description =models.TextField(max_length=100)
    Price = models.DecimalField(max_digits=7, decimal_places=2)
    image =models.ImageField(upload_to ='media/')

    def __str__ (self):
        return self.Name


