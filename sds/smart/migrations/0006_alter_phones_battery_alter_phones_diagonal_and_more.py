# Generated by Django 4.0.3 on 2022-05-06 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smart', '0005_alter_phones_sim'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phones',
            name='battery',
            field=models.IntegerField(verbose_name='Емкость батареи (мAч)'),
        ),
        migrations.AlterField(
            model_name='phones',
            name='diagonal',
            field=models.FloatField(verbose_name='Диагональ (")'),
        ),
        migrations.AlterField(
            model_name='phones',
            name='platform',
            field=models.CharField(choices=[('Android', 'Android'), ('IOS', 'IOS')], default='Android', max_length=100, verbose_name='Платформа'),
        ),
        migrations.AlterField(
            model_name='phones',
            name='price',
            field=models.IntegerField(verbose_name='Цена (₽)'),
        ),
        migrations.AlterField(
            model_name='phones',
            name='processor_frequency',
            field=models.IntegerField(verbose_name='Частота процессора (МГц)'),
        ),
        migrations.AlterField(
            model_name='phones',
            name='ram',
            field=models.IntegerField(verbose_name='Оперативная память (ГБ)'),
        ),
        migrations.AlterField(
            model_name='phones',
            name='rom',
            field=models.IntegerField(verbose_name='Постоянная память (ГБ)'),
        ),
        migrations.AlterField(
            model_name='phones',
            name='sim',
            field=models.IntegerField(choices=[(1, '1 SIM'), (2, '2 SIM')], default=1, verbose_name='Количество SIM'),
        ),
        migrations.AlterField(
            model_name='phones',
            name='warranty',
            field=models.IntegerField(verbose_name='Гарантия (Мес.)'),
        ),
    ]
