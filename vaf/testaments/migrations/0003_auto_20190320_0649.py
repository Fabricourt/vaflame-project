# Generated by Django 2.1.7 on 2019-03-20 03:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testaments', '0002_testament_partner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testament',
            name='Partner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
