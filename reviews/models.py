from django.db import models


class Review(models.Model):

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name