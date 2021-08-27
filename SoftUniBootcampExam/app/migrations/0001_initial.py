# Generated by Django 3.2.6 on 2021-08-27 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('bio', models.TextField()),
                ('birth_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=240)),
                ('value', models.CharField(db_index=True, max_length=240)),
                ('container', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.candidate')),
            ],
        ),
    ]
