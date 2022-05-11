# Generated by Django 4.0.3 on 2022-05-09 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smart', '0006_alter_phones_battery_alter_phones_diagonal_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tagis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_tag', models.CharField(max_length=255, verbose_name='Название тега')),
                ('filter', models.CharField(max_length=255, verbose_name='Поля фильтрации')),
            ],
        ),
        migrations.AlterModelOptions(
            name='phones',
            options={'ordering': ['id'], 'verbose_name': 'смартфон', 'verbose_name_plural': 'Смартфоны'},
        ),
        migrations.AlterField(
            model_name='phones',
            name='warranty',
            field=models.IntegerField(verbose_name='Гарантия (мес.)'),
        ),
        migrations.CreateModel(
            name='TagsPhones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smart.phones')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smart.tagis')),
            ],
        ),
    ]
