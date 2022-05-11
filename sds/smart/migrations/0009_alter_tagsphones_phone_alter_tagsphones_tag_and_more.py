# Generated by Django 4.0.3 on 2022-05-09 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smart', '0008_alter_tagis_options_alter_tagsphones_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tagsphones',
            name='phone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smart.phones'),
        ),
        migrations.AlterField(
            model_name='tagsphones',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smart.tagis'),
        ),
        migrations.AlterUniqueTogether(
            name='tagsphones',
            unique_together={('phone', 'tag')},
        ),
    ]
