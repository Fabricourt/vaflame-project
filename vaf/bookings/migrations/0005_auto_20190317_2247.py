# Generated by Django 2.1.7 on 2019-03-17 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0004_booking_unapproved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='unapproved',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
