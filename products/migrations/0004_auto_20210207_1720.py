# Generated by Django 3.1.6 on 2021-02-07 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210207_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(default='external-content.duckduckgo.com.jpeg', null=True, upload_to='products/'),
        ),
    ]
