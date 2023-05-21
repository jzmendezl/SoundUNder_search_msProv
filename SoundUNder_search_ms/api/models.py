from django.db import models

# Create your models here.

class Song(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    idSong =  models.IntegerField(max_length=100)

    class Meta: 
        verbose_name = 'Songs'
        verbose_name_plural = 'Songs'

    def __str__(self) :
        return self.name