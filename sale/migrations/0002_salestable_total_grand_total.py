# Generated by Django 4.2.7 on 2023-11-19 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='salestable',
            name='total_grand_total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
