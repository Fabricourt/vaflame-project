# Generated by Django 2.1.7 on 2019-03-17 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_auto_20190317_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='approved',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
