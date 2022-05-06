from django.db import models


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
    distance = models.ForeignKey(
        'Distance', null=True, blank=True, on_delete=models.SET_NULL)
    effort = models.CharField(max_length=254)
    description = models.TextField()
    week = models.CharField(max_length=254)
    day = models.CharField(max_length=254)

    def __str__(self):
        return self.effort
