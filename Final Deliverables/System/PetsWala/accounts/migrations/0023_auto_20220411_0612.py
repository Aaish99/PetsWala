# Generated by Django 3.2.9 on 2022-04-11 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_auto_20220411_0541'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='resc_addr_lat',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='request',
            name='resc_addr_lng',
            field=models.FloatField(blank=True, default=0),
        ),
    ]