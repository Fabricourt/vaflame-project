# Generated by Django 2.1.7 on 2019-03-20 03:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testaments', '0003_auto_20190320_0649'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testament',
            old_name='Partner',
            new_name='partner',
        ),
        migrations.RemoveField(
            model_name='testament',
            name='name',
        ),
    ]