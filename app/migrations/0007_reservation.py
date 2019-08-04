# Generated by Django 2.2.1 on 2019-07-19 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_lunch_photo_pics'),
    ]

    operations = [
        migrations.CreateModel(
            name='reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('time', models.CharField(max_length=100)),
                ('people', models.CharField(max_length=100)),
            ],
        ),
    ]