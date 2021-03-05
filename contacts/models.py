from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.core.files import File

from io import BytesIO
from PIL import Image, ImageOps

from django.db.models.signals import post_delete, pre_save
from django.dispatch.dispatcher import receiver


class Contact(models.Model):

    profile_picture = models.ImageField(upload_to='images/', blank=True)
    thumbnail = models.ImageField(upload_to='images/', blank=True)

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

        if self.profile_picture:

            # Create thumbnail
            raw_img = Image.open(self.profile_picture)
            corrected_img = ImageOps.exif_transpose(raw_img)
            square_img = self.crop_max_square(corrected_img)
            if square_img.height != 200:
                square_img = square_img.resize((200, 200), Image.LANCZOS)

            # Save thumbnail
            thumb_io = BytesIO()
            square_img.save(thumb_io, raw_img.format, quality=75)
            thumbnail = File(thumb_io, name=self.profile_picture.name)
            self.thumbnail = thumbnail

        super().save(*args, **kwargs)


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


@receiver(post_delete, sender=Contact)
def delete_images_from_S3(sender, instance, **kwargs):
    """
    'post_delete' model signal used to delete associated images from the
    S3 bucket when a contact is deleted. 'False' here ensures that the model
    is not saved after the image in question has been deleted.
    """
    instance.profile_picture.delete(False)
    instance.thumbnail.delete(False)
