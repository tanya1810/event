# Generated by Django 3.0.7 on 2020-07-30 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trading',
            name='multiplicationfactor',
        ),
    ]
