# Generated by Django 5.1 on 2024-08-22 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('employee_id', models.CharField(max_length=50, unique=True)),
                ('shift', models.CharField(blank=True, max_length=10)),
                ('week_off', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
