# Generated by Django 4.0.3 on 2022-05-05 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='mini_title',
        ),
    ]