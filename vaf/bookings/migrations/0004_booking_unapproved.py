# Generated by Django 2.1.7 on 2019-03-17 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0003_booking_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='unapproved',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
