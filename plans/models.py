from django.db import models
from django.contrib.auth.models import User



class Distance(models.Model):

    class Meta:
        verbose_name_plural = 'Distances'
    
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Session(models.Model):
    distance = models.ForeignKey('Distance', null=True, blank=True, on_delete=models.SET_NULL)
    type = models.CharField(max_length=254, null=True, blank=True)
    effort = models.CharField(max_length=254)
    description = models.TextField()
    week = models.CharField(max_length=254)
    day = models.CharField(max_length=254)

    def __str__(self):
        return self.effort


