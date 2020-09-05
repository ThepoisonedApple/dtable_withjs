from django.db import models

# Create your models here.

class Denemetablo(models.Model):
    rand_str = models.CharField(max_length=10)
    rand_int = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'denemetablo'