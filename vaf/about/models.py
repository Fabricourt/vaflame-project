from django.db import models
from datetime import datetime
from django.urls import reverse # Used to generate URLS by reversing the URL patterns
from django.contrib.auth.models import User  # Required to assign User as a debtor, buyer orseller
from datetime import date
from ckeditor.fields import RichTextField

class About(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    description = RichTextField(blank=True, null=True)
    photoa = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photob = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photoc = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photod = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photoe = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photof = models.ImageField(upload_to='photos/%Y/%m/%d/')
    
    class Meta:
        ordering = ['title']

    def get_absolute_url(self):
        """Returns the url to access a particular property instance."""
        return reverse('property-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.title