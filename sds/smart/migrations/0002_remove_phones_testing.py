# Generated by Django 4.0.3 on 2022-05-05 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phones',
            name='Testing',
        ),
    ]