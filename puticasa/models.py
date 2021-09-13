from django.db import models
from django.contrib.auth.models import AbstractUser
from users.models import User


# common enums
class Status(models.IntegerChoices):
    INACTIVE = 0
    ACTIVE = 1
    ARCHIVED = 2


# Create your models here.
class House(models.Model):

    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    status = models.IntegerField(choices=Status.choices, default=Status.ACTIVE)
    # automatically set date when creating
    start_date = models.DateTimeField(auto_now_add=True)
    # automatically set date when saving
    last_modified_date = models.DateTimeField(auto_now=True)
    end_date = models.DateTimeField(blank=True, null=True)

    users = models.ManyToManyField(User, through='Resident')

    def __str__(self):
        return self.name


class Resident(models.Model):

    class Type(models.IntegerChoices):
        GUEST = 0
        TENANT = 1
        ADMIN = 2

    status = models.IntegerField(choices=Status.choices, default=Status.ACTIVE)
    # automatically set date when creating
    start_date = models.DateTimeField(auto_now_add=True)
    # automatically set date when saving
    last_modified_date = models.DateTimeField(auto_now=True)
    end_date = models.DateTimeField(blank=True, null=True)

    type = models.IntegerField(choices=Type.choices, default=Type.GUEST)
    house = models.ForeignKey(House, related_name="residents", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="residents", on_delete=models.CASCADE)

    def __str__(self):
        return self.user.__str__() + ", living in " + self.house.__str__() + " as a " + self.get_type_display()


