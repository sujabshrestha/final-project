# Generated by Django 3.0.8 on 2020-09-28 17:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('discussion', '0007_auto_20200928_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='discussion',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='discussion',
            name='image',
            field=models.ImageField(default='default.jpg', null=True, upload_to='profile_pics'),
        ),
        migrations.AddField(
            model_name='discussion',
            name='username',
            field=models.CharField(default='', max_length=30),
        ),
    ]
