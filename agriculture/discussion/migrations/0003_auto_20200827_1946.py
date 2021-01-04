# Generated by Django 3.0.8 on 2020-08-27 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discussion', '0002_auto_20200827_1903'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='message',
            new_name='Message',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='phone',
            new_name='Phone',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='name',
        ),
        migrations.AddField(
            model_name='feedback',
            name='Name',
            field=models.CharField(default='', max_length=30),
        ),
    ]
