# Generated by Django 2.1.5 on 2019-02-04 10:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=500)),
                ('auth_uname', models.CharField(max_length=200)),
                ('auth_pwd', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.CharField(max_length=500)),
                ('b', models.CharField(max_length=500)),
                ('c', models.CharField(max_length=500)),
                ('d', models.CharField(max_length=500)),
            ],
        ),
    ]
