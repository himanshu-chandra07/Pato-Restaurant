# Generated by Django 2.2.1 on 2019-07-22 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20190722_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='nameq',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='phoneq',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
