# Generated by Django 2.1.5 on 2019-11-30 03:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_pricing'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pricing',
            old_name='pizza',
            new_name='item_pizza',
        ),
    ]
