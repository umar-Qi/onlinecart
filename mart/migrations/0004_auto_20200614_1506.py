# Generated by Django 3.0.7 on 2020-06-14 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mart', '0003_contact'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='contact',
            new_name='ClientInfo',
        ),
    ]
