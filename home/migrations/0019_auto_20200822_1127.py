# Generated by Django 3.0.7 on 2020-08-22 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20200820_0433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trading',
            name='percentage_for_sale',
            field=models.DecimalField(decimal_places=0, default=5, max_digits=3),
        ),
    ]
