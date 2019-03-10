from django.db import models
from datetime import datetime
from django.urls import reverse # Used to generate URLS by reversing the URL patterns
from ckeditor.fields import RichTextField
from PIL import Image

class Gallery(models.Model):
    title = models.CharField(max_length=100, blank=True, null=False)
    photo_gallery = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_7 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_8 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_9 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_10 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_11 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_12 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    gallery_date = models.DateTimeField(default=datetime.now, blank=True)
    description = RichTextField(blank=True, null=True)

    class Meta:
        ordering = ['title']

    def get_absolute_url(self):
        """Returns the url to access a particular property instance."""
        return reverse('property-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.title
