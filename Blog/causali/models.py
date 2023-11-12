from django.db import models

# Create your models here.

class Causali(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, blank=True, null=True)
    descrizione = models.CharField(max_length=50, blank=True, null=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'causali'
        verbose_name_plural = "Causali"

    def __str__(self):
        return self.nome
