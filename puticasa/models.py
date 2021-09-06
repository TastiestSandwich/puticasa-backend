from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class House(models.Model):

    class Status(models.IntegerChoices):
        INACTIVE = 0
        ACTIVE = 1
        ARCHIVED = 2

    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    status = models.IntegerField(choices=Status.choices, default=Status.ACTIVE)
    # automatically set date when creating
    start_date = models.DateTimeField(auto_now_add=True)
    # automatically set date when saving
    last_modified_date = models.DateTimeField(auto_now=True)
    end_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name

