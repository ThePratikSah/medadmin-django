# Generated by Django 4.2.6 on 2023-10-28 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_product_options_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='category',
            table='categories',
        ),
    ]