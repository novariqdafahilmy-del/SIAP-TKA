from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        GURU = "GURU", "Guru"
        SISWA = "SISWA", "Siswa"

    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.SISWA
    )

    def __str__(self):
        return self.username