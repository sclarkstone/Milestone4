# Generated by Django 3.2 on 2022-03-19 17:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0008_auto_20220319_1627'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='name',
        ),
        migrations.AddField(
            model_name='review',
            name='date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='order_number',
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.AddField(
            model_name='review',
            name='product_id',
            field=models.CharField(blank=True, max_length=3),
        ),
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='review',
            name='review',
            field=models.TextField(default='0'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='subject',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.OneToOneField(default='0', on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
