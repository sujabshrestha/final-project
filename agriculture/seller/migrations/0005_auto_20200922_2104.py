# Generated by Django 3.0.8 on 2020-09-22 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0004_auto_20200921_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='address',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='seller',
            name='phone',
            field=models.IntegerField(default=0),
        ),
    ]