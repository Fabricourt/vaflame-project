# Generated by Django 2.1.7 on 2019-03-16 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0003_auto_20190316_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
