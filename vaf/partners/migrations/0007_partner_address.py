# Generated by Django 2.1.7 on 2019-03-17 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0006_auto_20190316_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='address',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
