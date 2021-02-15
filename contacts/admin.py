from django.contrib import admin

from .models import Contact

from image_cropping import ImageCroppingMixin


class ContactAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass

admin.site.register(Contact, ContactAdmin)