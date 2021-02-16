from django import forms

from .models import Contact

# from image_cropping import ImageCropWidget


class ContactForm(forms.ModelForm):
    class Meta:

        model = Contact

        fields = (
            'profile_picture',
            'cropping',
            'first_name',
            'last_name',
            'nickname',
            'postal_address',
            'phone_number',
            'email_address',
            'linkedin_url',
            'twitter_url',
            'github_url',
            'personal_website'
        )
        """
        widgets = {
            'profile_picture': ImageCropWidget,
        }
        """
