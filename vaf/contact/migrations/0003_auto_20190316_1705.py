# Generated by Django 2.1.7 on 2019-03-16 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_sema'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sema',
            old_name='listing',
            new_name='partners',
        ),
        migrations.RenameField(
            model_name='sema',
            old_name='listing_id',
            new_name='partners_id',
        ),
    ]
