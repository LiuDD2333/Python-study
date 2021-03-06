# Generated by Django 2.1.5 on 2019-03-05 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datum', '0008_auto_20190305_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='object_list_all',
            name='Obs_stage',
            field=models.CharField(choices=[(0, 'current'), (1, 'past'), (2, 'future'), (3, 'removed')], default=0, max_length=30, verbose_name='观测阶段'),
        ),
        migrations.AlterField(
            model_name='object_list_all',
            name='mode',
            field=models.CharField(choices=[(0, 'observation'), (1, 'test')], default=0, max_length=30, verbose_name='模式'),
        ),
    ]
