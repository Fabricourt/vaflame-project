from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()
    photo1 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo2 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo3 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo4 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo5 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo6 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


