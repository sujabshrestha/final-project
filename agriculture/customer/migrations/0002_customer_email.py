# Generated by Django 3.0.8 on 2020-07-19 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.CharField(default='', max_length=255),
        ),
    ]
