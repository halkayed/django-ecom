# Generated by Django 3.1.6 on 2021-02-07 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20210207_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(default='no_image.jpeg', null=True, upload_to='products/'),
        ),
    ]