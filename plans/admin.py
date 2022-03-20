from django.contrib import admin
from .models import Distance
from .models import Session

# Register your models here.


class DistanceAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class SessionAdmin(admin.ModelAdmin):
    list_display = (
        'type',
        'week',
        'day',
        'effort',
        'description',
    )


admin.site.register(Distance, DistanceAdmin)
admin.site.register(Session, SessionAdmin)