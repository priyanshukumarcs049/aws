# Generated by Django 2.1.5 on 2019-02-15 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Index', '0006_auto_20190215_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='notification',
            name='place',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='notification',
            name='time',
            field=models.CharField(max_length=50),
        ),
    ]
