# Generated by Django 5.0.1 on 2024-01-12 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_rename_adoption1_adoption'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Adoption',
            new_name='Adoption1',
        ),
    ]