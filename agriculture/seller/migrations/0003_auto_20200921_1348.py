# Generated by Django 3.0.8 on 2020-09-21 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0002_seller_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='image',
            field=models.ImageField(default='/profile_pics/default.jpg', upload_to='profile_pics'),
        ),
    ]
