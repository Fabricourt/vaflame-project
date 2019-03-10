from django.db import models
from datetime import datetime
from django.urls import reverse # Used to generate URLS by reversing the URL patterns
from django.contrib.auth.models import User  # Required to assign User as a Partner
from datetime import date
from ckeditor.fields import RichTextField



class Team(models.Model):
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    identity_number = models.CharField(max_length=100, blank=False, null=False)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    description = RichTextField(blank=True, help_text='e.g partner role, organisation, ministry' )
    zip_code = models.CharField(max_length=20)
    phone = models.IntegerField()
    email = models.CharField(max_length=50)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)
    is_published = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['last_name', 'first_name']


    def __str__(self):
        """String for representing the Model object."""
        return '{0}, {1}'.format(self.last_name, self.first_name)

    def get_absolute_url(self):
        """Returns the url to access a particular location instance."""
        return reverse('owner-detail', args=[str(self.id)])


