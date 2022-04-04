from django.contrib import admin
from .models import Distance
from .models import Session

# Register your models here.


class DistanceAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'product_id',
        'duration',
        'instructions',
    )


class SessionAdmin(admin.ModelAdmin):
    list_display = (
        'week',
        'day',
        'effort',
        'description',
    )


admin.site.register(Distance, DistanceAdmin)
admin.site.register(Session, SessionAdmin)