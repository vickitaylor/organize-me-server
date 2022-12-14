from django.db import models
from django.contrib.auth.models import User


class Organizer(models.Model):
    """ the organizer model, inherits properties form the parent class model User.
    """
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="user")
    picture = models.CharField(max_length=500)
    approved_users = models.ManyToManyField("Organizer", through="Family", related_name="app_user")

    @property
    def approved(self):
        return self.__approved

    @approved.setter
    def approved(self, value):
        self.__approved = value
