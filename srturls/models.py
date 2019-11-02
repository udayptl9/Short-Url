from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Urls(models.Model):
    title = models.CharField(max_length=50)
    fullurl = models.CharField(max_length=200)
    creater = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Urls'