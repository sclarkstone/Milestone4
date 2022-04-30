from django.contrib import admin
from .models import Review

# Register your models here.


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'subject',
        'review',
        'rating',
        'product_id',
        'order_number',
        'date',

    )


admin.site.register(Review, ReviewAdmin)
