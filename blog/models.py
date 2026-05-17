from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):

    CATEGORIAS = (
        ('python', 'Python'),
        ('django', 'Django'),
        ('backend', 'Backend'),
        ('api', 'API'),
    )

    titulo = models.CharField(
        max_length=200
    )

    categoria = models.CharField(
        max_length=50,
        choices=CATEGORIAS
    )

    texto = models.TextField()

    autor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.titulo