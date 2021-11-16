from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Thing(models.Model):
    name = models.CharField(max_length=256)
    rating = models.IntegerField(default=0)
    color = models.CharField(max_length=256)
    reviewer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name
