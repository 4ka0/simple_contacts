from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:

        model = Contact

        fields = (
            'profile_picture',
            'first_name',
            'last_name',
            'nickname',
            'postal_address',
            'phone_number',
            'email_address',
            'linkedin_url',
            'twitter_url',
            'github_url',
            'personal_website',
        )
