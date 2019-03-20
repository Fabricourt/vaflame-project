# Generated by Django 2.1.7 on 2019-03-20 02:02

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Testament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('ministry_name', models.CharField(blank=True, max_length=200, null=True)),
                ('message', ckeditor.fields.RichTextField(blank=True, max_length=999, null=True)),
                ('post_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
    ]
