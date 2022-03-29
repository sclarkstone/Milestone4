from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver


class Distance(models.Model):

    class Meta:
        verbose_name_plural = 'Distances'
    
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    duration = models.CharField(max_length=254, null=True, blank=True)
    product_id = models.CharField(max_length=254, null=True, blank=True)
    instructions = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

    def get_duration(self):
        return self.duration

    def get_instructions(self):
        return self.instructions


class Session(models.Model):
    distance = models.ForeignKey('Distance', null=True, blank=True, on_delete=models.SET_NULL)
    type = models.CharField(max_length=254, null=True, blank=True)
    effort = models.CharField(max_length=254)
    description = models.TextField()
    week = models.CharField(max_length=254)
    day = models.CharField(max_length=254)

    def __str__(self):
        return self.effort
