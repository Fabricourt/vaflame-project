from django.db import models
from datetime import datetime


from ckeditor.fields import RichTextField

class Booking(models.Model):
  user_id = models.IntegerField(blank=True, null=True)
  ministry_name = models.CharField(max_length=200, blank=True, null=True)
  email = models.CharField(max_length=100, blank=True, null=True)
  address = models.CharField(max_length=200, blank=True, null=True)
  phone_number = models.CharField(max_length=100, blank=True, null=True)
  ministry_location = models.CharField(max_length=100, blank=True, null=True)
  county = models.CharField(max_length=100, blank=True, null=True)
  description = RichTextField(blank=True, null=True)
  is_published = models.BooleanField(default=True)
  booking_date = models.DateTimeField(blank=True, null=True)
  return_date = models.DateTimeField(blank=True, null=True)
  def __str__(self):
    return self.title



