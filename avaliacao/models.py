from django.contrib.auth.models import User
from django.db import models

class Avaliacao(models.Model):
    # nome nos comentarios
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    # comentario
    comentario = models.TextField(null=True, blank=True)
    #nota da avaliaçao
    nota = models.DecimalField(max_digits=3, decimal_places=2)
    #data da avaliacao
    data= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.usuario.username
