from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
# Create your models here.


class tags(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Picture(models.Model):
    image = models.ImageField(upload_to='articles/')
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFill(100, 50)],
                                     format='JPEG',
                                     options={'quality': 60})
    pub_date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(tags)
    description = models.TextField(blank=True)
    
    @classmethod
    def search_by_title(cls, search_term):
        images = cls.objects.filter(title__ifcontains=search_term)

        return images
