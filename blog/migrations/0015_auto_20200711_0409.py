# Generated by Django 3.0.7 on 2020-07-11 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20200711_0408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='title',
            field=models.CharField(default='draft', max_length=24),
        ),
    ]