# Generated by Django 3.1.2 on 2020-10-31 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_profile_budget_left'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='budget',
            field=models.FloatField(),
        ),
    ]
