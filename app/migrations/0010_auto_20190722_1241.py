# Generated by Django 2.2.1 on 2019-07-22 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20190722_1240'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='phone',
            new_name='phoneq',
        ),
    ]
