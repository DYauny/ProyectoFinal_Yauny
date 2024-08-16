from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avateres', null=True, blank = True)

    def __str__(self):
        return f"Imagen de: {self.user} - {self.imagen}"   #f"Imagen de: {self.user.username}


