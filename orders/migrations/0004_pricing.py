# Generated by Django 2.1.5 on 2019-11-30 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20191130_1130'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizza', models.CharField(choices=[('RCH', 'Regular Cheese'), ('R1T', 'Regular 1 topping'), ('R2T', 'Regular 2 topping'), ('R3T', 'Regular 3 topping'), ('RSP', 'Regular Special')], default='RCH', max_length=64)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
    ]
