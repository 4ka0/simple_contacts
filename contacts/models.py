from django.db import models
from django.urls import reverse


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50, blank=True)
    postal_address = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=50, blank=True)
    email_address = models.EmailField(max_length=250, blank=True)
    linkedin_url = models.URLField(max_length=200, blank=True)
    twitter_url = models.URLField(max_length=200, blank=True)
    personal_website = models.URLField(max_length=200, blank=True)
    created_on = models.DateField(auto_now_add=True)
    last_modified_on = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'contacts'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('contact_detail', args=[str(self.id)])