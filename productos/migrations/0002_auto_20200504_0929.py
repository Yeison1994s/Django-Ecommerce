# Generated by Django 3.0.5 on 2020-05-04 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='imagen',
            field=models.ImageField(upload_to='productos/'),
        ),
    ]
