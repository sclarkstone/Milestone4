from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_subject = models.CharField(max_length=20, null=True, blank=True)
    default_review = models.CharField(max_length=500, null=True, blank=True)
    default_rating = models.CharField(max_length=4, null=True, blank=True)

    def __str__(self):
        return self.user.username