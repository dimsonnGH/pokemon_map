# Generated by Django 2.2.3 on 2020-03-21 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0013_auto_20200321_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='test_time',
            field=models.DateTimeField(default=None, null=True, verbose_name='test время'),
        ),
    ]
