from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Person(AbstractUser):
    email = models.EmailField(unique=True, max_length=255,verbose_name="Email Address")
    country = models.CharField(max_length=255, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(choices=(("Male","male"),("Female","female"),("Prefer not to say","no_preference")),max_length=255)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "People"

    def __str__(self) -> str:
        return self.email

    