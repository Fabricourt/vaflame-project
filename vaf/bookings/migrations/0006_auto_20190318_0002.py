# Generated by Django 2.1.7 on 2019-03-17 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0005_auto_20190317_2247'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='last_name',
        ),
    ]
