# Generated by Django 3.0.7 on 2020-07-11 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20200711_0356'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='title',
            field=models.CharField(default=None, max_length=24),
        ),
    ]
