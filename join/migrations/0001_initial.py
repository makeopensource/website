# Generated by Django 3.2.6 on 2021-08-10 18:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('email', models.EmailField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('major', models.CharField(max_length=300)),
                ('exp_grad_year', models.IntegerField(choices=[(2021, '2021'), (2022, '2022'), (2023, '2023'), (2024, '2024'), (2025, '2025'), (2026, '2026')])),
                ('join_date', models.DateField(default=datetime.date.today, editable=False)),
            ],
        ),
    ]
