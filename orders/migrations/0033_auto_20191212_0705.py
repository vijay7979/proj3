# Generated by Django 2.1.5 on 2019-12-11 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0032_auto_20191208_2222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='additions',
        ),
        migrations.AddField(
            model_name='order',
            name='additions',
            field=models.ManyToManyField(blank=True, to='orders.Addition'),
        ),
    ]
