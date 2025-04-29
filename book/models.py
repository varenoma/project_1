from django.db import models

# Create your models here.
class Book(models.Model):
    nomi = models.CharField(max_length=100)
    muallif = models.CharField(max_length=100)
    yaratilgan_yil = models.PositiveIntegerField()
    til = models.CharField(max_length=30)
    janr = models.CharField(max_length=100)
    betlar_soni = models.IntegerField()
    qisqacha_mazmuni = models.TextField()
    
    def __str__(self):
        return self.nomi
    
    class Meta:
        db_table = 'book'