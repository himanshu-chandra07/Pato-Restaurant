# Generated by Django 2.2.1 on 2019-07-22 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20190722_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='people',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='time',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
