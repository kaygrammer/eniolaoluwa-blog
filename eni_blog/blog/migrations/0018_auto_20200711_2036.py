# Generated by Django 3.0.7 on 2020-07-11 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_aboutme'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutme',
            old_name='title',
            new_name='name',
        ),
    ]
