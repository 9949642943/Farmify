# Generated by Django 3.1 on 2020-10-30 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auths', '0004_auto_20201030_1024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_dealer',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_farmer',
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('farmer', 'FARMER'), ('dealer', 'DEALER')], default='farmer', max_length=6),
        ),
    ]
