# Generated by Django 2.1.5 on 2019-12-01 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_auto_20191130_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='special',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=3),
        ),
    ]