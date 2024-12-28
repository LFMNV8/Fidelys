from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField()
    image = models.ImageField(upload_to='profile_pics/', default='default-profile.png')

    def __str__(self):
        return self.user.username