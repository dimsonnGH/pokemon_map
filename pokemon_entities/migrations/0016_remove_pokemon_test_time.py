# Generated by Django 2.2.3 on 2020-03-21 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0015_auto_20200321_1939'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='test_time',
        ),
    ]
