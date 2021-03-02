from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone

from contacts.models import Contact


# need to check using an image and a thumbnail

class ContactModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Contact.objects.create(

            first_name="Test",
            last_name="User",
            nickname="Tester",

            postal_address="23 Test Avenue, Test Road, Testville, Testshire, TS3 3TY, UK",
            phone_number="090-8745-2365",
            email_address="testuser@email.com",

            linkedin_url="https://www.linkedin.com/testuser",
            twitter_url="https://www.twitter.com/testuser",
            github_url="https://www.github.com/testuser",
            personal_website="https://www.testuser.com",
        )

    # Test field labels

    def test_first_name_label(self):
        contact = Contact.objects.get(id=1)
        field_label = contact._meta.get_field("first_name").verbose_name
        self.assertEqual(field_label, "first name")

    def test_last_name_label(self):
        contact = Contact.objects.get(id=1)
        field_label = contact._meta.get_field("last_name").verbose_name
        self.assertEqual(field_label, "last name")

    def test_nickname_label(self):
        contact = Contact.objects.get(id=1)
        field_label = contact._meta.get_field("nickname").verbose_name
        self.assertEqual(field_label, "nickname")

    def test_postal_address_label(self):
        contact = Contact.objects.get(id=1)
        field_label = contact._meta.get_field("postal_address").verbose_name
        self.assertEqual(field_label, "postal address")

    def test_phone_number_label(self):
        contact = Contact.objects.get(id=1)
        field_label = contact._meta.get_field("phone_number").verbose_name
        self.assertEqual(field_label, "phone number")

    def test_email_address_label(self):
        contact = Contact.objects.get(id=1)
        field_label = contact._meta.get_field("email_address").verbose_name
        self.assertEqual(field_label, "email address")

    def test_linkedin_url_label(self):
        contact = Contact.objects.get(id=1)
        field_label = contact._meta.get_field("linkedin_url").verbose_name
        self.assertEqual(field_label, "linkedin url")

    def test_twitter_url_label(self):
        contact = Contact.objects.get(id=1)
        field_label = contact._meta.get_field("twitter_url").verbose_name
        self.assertEqual(field_label, "twitter url")

    def test_github_url_label(self):
        contact = Contact.objects.get(id=1)
        field_label = contact._meta.get_field("github_url").verbose_name
        self.assertEqual(field_label, "github url")

    def test_personal_website_label(self):
        contact = Contact.objects.get(id=1)
        field_label = contact._meta.get_field("personal_website").verbose_name
        self.assertEqual(field_label, "personal website")

    def test_created_on_label(self):
        contact = Contact.objects.get(id=1)
        field_label = contact._meta.get_field("created_on").verbose_name
        self.assertEqual(field_label, "created on")

    # Test field max_lengths

    def test_first_name_max_length(self):
        contact = Contact.objects.get(id=1)
        max_length = contact._meta.get_field("first_name").max_length
        self.assertEqual(max_length, 50)

    def test_last_name_max_length(self):
        contact = Contact.objects.get(id=1)
        max_length = contact._meta.get_field("last_name").max_length
        self.assertEqual(max_length, 50)

    def test_nickname_max_length(self):
        contact = Contact.objects.get(id=1)
        max_length = contact._meta.get_field("nickname").max_length
        self.assertEqual(max_length, 50)

    def test_postal_address_max_length(self):
        contact = Contact.objects.get(id=1)
        max_length = contact._meta.get_field("postal_address").max_length
        self.assertEqual(max_length, 200)

    def test_phone_number_max_length(self):
        contact = Contact.objects.get(id=1)
        max_length = contact._meta.get_field("phone_number").max_length
        self.assertEqual(max_length, 50)

    def test_email_address_max_length(self):
        contact = Contact.objects.get(id=1)
        max_length = contact._meta.get_field("email_address").max_length
        self.assertEqual(max_length, 200)

    def test_object_instatiation(self):
        contact = Contact.objects.get(id=1)

        self.assertEqual(contact.first_name, "Test")
        self.assertNotEqual(contact.first_name, "")

        self.assertEqual(contact.last_name, "User")
        self.assertNotEqual(contact.last_name, "")

        self.assertEqual(contact.nickname, "Tester")
        self.assertNotEqual(contact.nickname, "")

        self.assertEqual(contact.postal_address, "23 Test Avenue, Test Road, Testville, Testshire, TS3 3TY, UK")
        self.assertNotEqual(contact.last_name, "")

        self.assertEqual(contact.phone_number, "090-8745-2365")
        self.assertNotEqual(contact.phone_number, "")

        self.assertEqual(contact.email_address, "testuser@email.com")
        self.assertNotEqual(contact.email_address, "")

        self.assertEqual(contact.linkedin_url, "https://www.linkedin.com/testuser")
        self.assertNotEqual(contact.linkedin_url, "")

        self.assertEqual(contact.twitter_url, "https://www.twitter.com/testuser")
        self.assertNotEqual(contact.twitter_url, "")

        self.assertEqual(contact.github_url, "https://www.github.com/testuser")
        self.assertNotEqual(contact.github_url, "")

        self.assertEqual(contact.personal_website, "https://www.testuser.com")
        self.assertNotEqual(contact.personal_website, "")

    def test_get_absolute_url(self):
        contact = Contact.objects.get(id=1)
        self.assertEqual(contact.get_absolute_url(), '/1/')

    def test_str_representation(self):
        contact = Contact.objects.get(id=1)
        expected_object_name = f'{contact.first_name} {contact.last_name}'
        self.assertEqual(expected_object_name, str(contact))
