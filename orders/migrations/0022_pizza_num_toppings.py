# Generated by Django 2.1.5 on 2019-12-05 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0021_auto_20191205_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='num_toppings',
            field=models.IntegerField(choices=[(0, 'None'), (1, 'One'), (2, 'Two'), (3, 'Three')], default=0, max_length=2),
        ),
    ]
