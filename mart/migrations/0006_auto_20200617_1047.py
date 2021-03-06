# Generated by Django 3.0.7 on 2020-06-17 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mart', '0005_orders'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=5000)),
                ('name', models.CharField(max_length=90)),
                ('email', models.CharField(max_length=25)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=10)),
                ('zip_code', models.CharField(max_length=7)),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
        migrations.DeleteModel(
            name='Orders',
        ),
    ]
