# Generated by Django 3.1.4 on 2021-01-02 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_product_fcomposition'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='product_category',
            field=models.CharField(default='', max_length=255),
        ),
    ]