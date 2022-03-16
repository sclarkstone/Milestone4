from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):

    class Meta:
        verbose_name_plural = 'Reviews'
    
    name = models.CharField(max_length=254)
    subject = models.CharField(max_length=254, null=True, blank=True)
    review = models.CharField(max_length=500, null=True, blank=True)
    rating = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name
