# Generated by Django 3.1.7 on 2021-04-19 03:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('idealab', '0002_auto_20210419_0337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='idea',
            name='created_date',
        ),
        migrations.AddField(
            model_name='idea',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date released'),
            preserve_default=False,
        ),
    ]
