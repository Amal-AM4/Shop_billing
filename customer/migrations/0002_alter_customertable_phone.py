# Generated by Django 4.2.7 on 2023-11-06 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customertable',
            name='phone',
            field=models.CharField(max_length=13, unique=True),
        ),
    ]
