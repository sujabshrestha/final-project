# Generated by Django 3.0.8 on 2020-10-03 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_review_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='climate',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='product',
            name='growingperiod',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='product',
            name='healthbenifits',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='product',
            name='p_area',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='product',
            name='p_type',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='product',
            name='soilfertility',
            field=models.CharField(default='', max_length=30),
        ),
    ]
