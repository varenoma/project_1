from django.db import models

# Create your models here.


class Product(models.Model):
    nomi = models.CharField(max_length=200)
    malumoti = models.TextField()
    narxi = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.nomi

    class Meta:
        db_table = 'product'