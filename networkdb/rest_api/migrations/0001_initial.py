# Generated by Django 2.2 on 2019-04-14 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('hostname', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('make', models.CharField(blank=True, default='', max_length=100)),
                ('model', models.CharField(blank=True, default='', max_length=100)),
            ],
            options={
                'ordering': ('hostname',),
            },
        ),
        migrations.CreateModel(
            name='Sites',
            fields=[
                ('site_code', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('site_short_code', models.CharField(blank=True, default='', max_length=100)),
            ],
        ),
    ]