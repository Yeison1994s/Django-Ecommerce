# Generated by Django 3.0.5 on 2020-05-08 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0004_auto_20200508_1741'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='categoriaProducto',
            new_name='Category',
        ),
    ]
