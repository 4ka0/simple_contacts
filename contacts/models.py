from django.db import models
from django.urls import reverse
from django.utils import timezone

from image_cropping import ImageCropField, ImageRatioField


class Contact(models.Model):
    profile_picture = ImageCropField(upload_to='images/', blank=True, null=True)
    cropping = ImageRatioField('profile_picture', '200x200')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50, blank=True)
    postal_address = models.CharField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=50, blank=True)
    email_address = models.EmailField(max_length=200, blank=True)
    linkedin_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    personal_website = models.URLField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    last_modified_on = models.DateTimeField(timezone.now(), null=True)

    class Meta:
        verbose_name_plural = 'contacts'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('contact_detail', args=[str(self.pk)])