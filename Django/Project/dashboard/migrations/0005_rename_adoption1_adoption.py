# Generated by Django 5.0.1 on 2024-01-12 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_rename_adoption_adoption1'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Adoption1',
            new_name='Adoption',
        ),
    ]
