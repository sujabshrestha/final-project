# Generated by Django 3.0.8 on 2020-10-06 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20201005_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='fcomposition',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
    ]
