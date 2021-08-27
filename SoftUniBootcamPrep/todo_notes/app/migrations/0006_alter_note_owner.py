# Generated by Django 3.2.6 on 2021-08-23 14:19

import app.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_note_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='owner',
            field=models.ForeignKey(default=app.models.Profile, editable=False, on_delete=django.db.models.deletion.CASCADE, to='app.profile'),
        ),
    ]