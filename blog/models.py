from django.db import models

# Create your models here.
class Blog(models.Model):
    nomi = models.CharField(max_length=200)
    bio = models.TextField()
    yaratilgan_vaqt = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nomi
    
    class Meta:
        db_table = 'blog'