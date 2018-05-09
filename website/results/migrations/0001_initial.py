# Generated by Django 2.0.5 on 2018-05-09 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lists',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mapname', models.CharField(max_length=100)),
                ('key', models.CharField(default='', max_length=100)),
                ('value', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Maps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mapname', models.CharField(max_length=100)),
                ('cityname', models.CharField(max_length=100)),
                ('lat', models.CharField(max_length=10)),
                ('lon', models.CharField(max_length=10)),
                ('infotitle', models.CharField(default='', max_length=100)),
                ('infomsg', models.FloatField(max_length=100)),
                ('infotitle2', models.CharField(default='', max_length=100)),
                ('infomsg2', models.CharField(default='', max_length=100)),
                ('infotitle3', models.CharField(default='', max_length=100)),
                ('infomsg3', models.CharField(default='', max_length=100)),
                ('infotitle4', models.CharField(default='', max_length=100)),
                ('infomsg4', models.CharField(default='', max_length=100)),
                ('infotitle5', models.CharField(default='', max_length=100)),
                ('infomsg5', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
