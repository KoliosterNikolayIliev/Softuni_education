# Generated by Django 3.1.2 on 2020-10-31 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20201031_1556'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='image_url',
            new_name='Link_to_image',
        ),
    ]
