# Generated by Django 2.2.3 on 2020-03-09 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0004_auto_20200309_1327'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemon',
            old_name='photo',
            new_name='image',
        ),
    ]
