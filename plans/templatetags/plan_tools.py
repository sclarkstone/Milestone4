import datetime

from django import template


register = template.Library()

@register.filter(name='calc_expire_date')
def calc_expire_date(value):
    return value + datetime.timedelta(days=45)