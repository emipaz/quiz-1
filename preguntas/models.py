from django.db import models

# Create your models here.
class Pregunta(models.Model):
    pregunta = models.TextField(max_length=500)

    def __str__(self):
        return self.pregunta



class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, related_name='respuestas')
    respuesta = models.CharField(max_length=200)
    correctas = models.IntegerField(blank=True,null=True)


    def __str__(self):
        return self.respuesta