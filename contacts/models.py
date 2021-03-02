from django.db import models
from django.urls import reverse
from django.utils import timezone

from io import BytesIO
from PIL import Image, ImageOps

from django.core.files.storage import default_storage

# from imagekit.models import ImageSpecField
# from imagekit.processors import SmartResize


class Contact(models.Model):

    profile_picture = models.ImageField(upload_to='images/', blank=True)

    """
    thumbnail = ImageSpecField(
        source='profile_picture',
        processors=[SmartResize(200, 200)],
        format='PNG',
        options={'quality': 60}
    )
    """

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

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.profile_picture:
            raw_img = Image.open(self.profile_picture)
            corrected_img = ImageOps.exif_transpose(raw_img)
            square_img = self.crop_max_square(corrected_img)
            if square_img.height != 300:
                square_img = square_img.resize((300, 300), Image.LANCZOS)
            memfile = BytesIO()
            square_img.save(memfile, 'JPEG', quality=75)
            default_storage.save(self.profile_picture.name, memfile)
            memfile.close()


    def crop_center(self, img, crop_width, crop_height):
        img_width, img_height = img.size
        cropped_img = img.crop((
            (img_width - crop_width) // 2,
            (img_height - crop_height) // 2,
            (img_width + crop_width) // 2,
            (img_height + crop_height) // 2
        ))
        return cropped_img


    def crop_max_square(self, img):
        max_square = self.crop_center(img, min(img.size), min(img.size))
        return max_square