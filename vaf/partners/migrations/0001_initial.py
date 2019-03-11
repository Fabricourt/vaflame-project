# Generated by Django 2.1.7 on 2019-03-10 17:45

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('identity_number', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('date_of_death', models.DateField(blank=True, null=True, verbose_name='Died')),
                ('description', ckeditor.fields.RichTextField(blank=True, help_text='e.g partner role, organisation, ministry')),
                ('zip_code', models.CharField(max_length=20)),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
                ('is_published', models.BooleanField(default=False)),
                ('Membership_date', models.DateTimeField(blank=True, default=datetime.datetime.now, help_text='Date when partner joined')),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
    ]