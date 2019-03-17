from django.db import models
from datetime import datetime
from django.urls import reverse # Used to generate URLS by reversing the URL patterns
from django.contrib.auth.models import User  # Required to assign User as a Partner
from datetime import date
from ckeditor.fields import RichTextField
from team.models import Team



class Partner(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    team = models.ForeignKey(Team, on_delete=models.DO_NOTHING, null=True, blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    ministry_name = models.CharField(max_length=200, blank=True, null=True)
    ministry_location = models.CharField(max_length=100, blank=True, null=True)
    county = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    identity_number = models.CharField(max_length=100, blank=False, null=False)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    description = RichTextField(blank=True, help_text='e.g partner role, organisation, ministry' )
    zip_code = models.CharField(max_length=20)
    address = models.CharField(max_length=50, null=True, blank=True)
    phone = models.IntegerField()
    email = models.CharField(max_length=50)
    is_published = models.BooleanField(default=False)
    membership_date = models.DateTimeField(default=datetime.now, blank=True, null=True, help_text='Date when partner joined')
    def __str__(self):
        return self.title

