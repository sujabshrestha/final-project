# Generated by Django 3.0.8 on 2020-10-03 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20201003_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='climate',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='product',
            name='growingperiod',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='product',
            name='p_area',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='product',
            name='p_type',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='product',
            name='soilfertility',
            field=models.CharField(default='', max_length=300),
        ),
    ]