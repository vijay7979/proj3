# Generated by Django 2.1.5 on 2019-11-30 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_remove_order_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pasta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('BCM', 'Baked Ziti w/Meatballs'), ('BCC', 'Baked Ziti w/Chicken')], default=('BCZ', 'Baked Ziti w/Mozzarella'), max_length=64)),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='price',
        ),
        migrations.RemoveField(
            model_name='price',
            name='size',
        ),
        migrations.AddField(
            model_name='order',
            name='size',
            field=models.CharField(choices=[('Small', 'Small'), ('Large', 'Large')], default='Large', max_length=10),
        ),
    ]