from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)

    # Evitar conflito de relacionamentos reversos com 'groups' e 'user_permissions'
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Altere o nome do relacionamento reverso
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions_set',  # Altere o nome do relacionamento reverso
        blank=True
    )

    def __str__(self):
        return self.username