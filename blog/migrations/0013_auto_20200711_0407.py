# Generated by Django 3.0.7 on 2020-07-11 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_about_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='title',
            field=models.CharField(default=True, max_length=24),
        ),
    ]