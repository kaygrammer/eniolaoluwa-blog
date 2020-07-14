# Generated by Django 3.0.7 on 2020-07-11 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20200711_0331'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='Body',
            new_name='body',
        ),
        migrations.AddField(
            model_name='about',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10),
        ),
    ]