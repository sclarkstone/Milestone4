# Generated by Django 3.2 on 2022-03-22 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0013_auto_20220322_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]