# Generated by Django 3.0.7 on 2020-07-02 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mart', '0010_order_source'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='source',
        ),
    ]
