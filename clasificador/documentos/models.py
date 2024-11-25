from django.db import models

class Documento(models.Model):
    archivo = models.FileField(upload_to="archivos/")
    clasificacion = models.CharField(max_length=50, blank=True)
    puntaje = models.FloatField(null=True, blank=True)
    cargado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.archivo.name
from django.db import models

# Create your models here.
