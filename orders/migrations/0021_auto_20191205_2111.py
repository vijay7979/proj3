# Generated by Django 2.1.5 on 2019-12-05 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0020_remove_order_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='pasta',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='pasta',
            name='size',
            field=models.CharField(choices=[('Small', 'Small'), ('Large', 'Large')], default='Large', max_length=20),
        ),
        migrations.AddField(
            model_name='pizza',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='pizza',
            name='size',
            field=models.CharField(choices=[('Small', 'Small'), ('Large', 'Large')], default='Large', max_length=20),
        ),
        migrations.AddField(
            model_name='salad',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='salad',
            name='size',
            field=models.CharField(choices=[('Small', 'Small'), ('Large', 'Large')], default='Large', max_length=20),
        ),
        migrations.AddField(
            model_name='sub',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='sub',
            name='size',
            field=models.CharField(choices=[('Small', 'Small'), ('Large', 'Large')], default='Large', max_length=20),
        ),
    ]
