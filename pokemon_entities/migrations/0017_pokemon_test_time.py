# Generated by Django 2.2.3 on 2020-03-21 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0016_remove_pokemon_test_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='test_time',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='test время'),
        ),
    ]
