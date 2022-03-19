from django.db import models


class Review(models.Model):

    name = models.CharField(max_length=254)
    subject = models.CharField(max_length=20, null=True, blank=True)
    review = models.TextField(null=False, blank=False)
    rating = models.IntegerField(default=0, null=False, blank=False)
    product_id = models.CharField(max_length=3, null=False, blank=True)
    order_number = models.CharField(max_length=32, null=False, blank=True)
    date = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.name