from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField




class Testimonial(models.Model):
    partner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    testimony = RichTextField (null=True, blank=True)
    is_published = models.BooleanField(default=True)
    def __str__(self):
        return f'{self.partner} {self.date_posted}'
    
    def save(self, **kwargs):
        super().save()
