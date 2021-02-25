from django.test import TestCase, SimpleTestCase

from contacts.forms import ContactForm


class CustomUserCreationFormTests(TestCase):

    def test_contact_form_field_labels(self):
        form = ContactForm()
        self.assertTrue(form.fields["first_name"].label == "First name")
        self.assertTrue(form.fields["last_name"].label == "Last name")
        self.assertTrue(form.fields["nickname"].label == "Nickname")
        self.assertTrue(form.fields["postal_address"].label == "Postal address")
        self.assertTrue(form.fields["phone_number"].label == "Phone number")
        self.assertTrue(form.fields["email_address"].label == "Email address")
        self.assertTrue(form.fields["linkedin_url"].label == "LinkedIn URL")
        self.assertTrue(form.fields["twitter_url"].label == "Twitter URL")
        self.assertTrue(form.fields["github_url"].label == "GitHub URL")
        self.assertTrue(form.fields["personal_website"].label == "Personal website")
        self.assertTrue(form.fields["profile_picture"].label == "Profile picture")

    def test_contact_form_required_fields(self):
        form = ContactForm()
        self.assertTrue(form.fields["first_name"].required)
        self.assertTrue(form.fields["last_name"].required)
        self.assertFalse(form.fields["nickname"].required)
        self.assertFalseform.fields["postal_address"].required)
        self.assertFalse(form.fields["phone_number"].required)
        self.assertFalse(form.fields["email_address"].required)
        self.assertFalse(form.fields["linkedin_url"].required)
        self.assertFalse(form.fields["twitter_url"].required)
        self.assertFalse(form.fields["github_url"].required)
        self.assertFalse(form.fields["personal_website"].required)
        self.assertFalse(form.fields["profile_picture"].required)

    def test_contact_form_field_maxlengths(self):
        form = ContactForm()
        self.assertTrue(form.fields["first_name"].max_length == 50)
        self.assertTrue(form.fields["last_name"].max_length == 50)
        self.assertTrue(form.fields["nickname"].max_length == 50)
        self.assertTrue(form.fields["postal_address"].max_length == 200)
        self.assertTrue(form.fields["phone_number"].max_length == 50)
        self.assertTrue(form.fields["email_address"].max_length == 200)

    def test_custom_user_creation_form_when_valid(self):
        form = ContactForm(
            {
                'first_name': "Test",
                'last_name: "User",
                'nickname': "Tester",
                'postal_address': "23 Test Avenue, Test Road, Testville, Testshire, TS3 3TY, UK",
                'phone_number': "080-1236-9874",
                'email_address': "testuser@email.com",
                'linkedin_url': "https://www.linkedin.com/testuser",
                'twitter_url': "https://www.twitter.com/testuser",
                'github_url': "https://www.github.com/testuser",
                'personal_website': "https://www.testuser.net",
            }
        )

        self.assertTrue(form.is_bound)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.errors, {})
        self.assertEqual(form.errors.as_text(), "")

        self.assertEqual(form.cleaned_data["first_name"], "Test")
        self.assertEqual(form.cleaned_data["last_name"], "User")
        self.assertEqual(form.cleaned_data["nickname"], "Tester")
        self.assertEqual(form.cleaned_data["postal_address"], "23 Test Avenue, Test Road, Testville, Testshire, TS3 3TY, UK")
        self.assertEqual(form.cleaned_data["phone_number"], "080-1236-9874")
        self.assertEqual(form.cleaned_data["email_address"], "testuser@email.com")
        self.assertEqual(form.cleaned_data["linkedin_url"], "https://www.linkedin.com/testuser")
        self.assertEqual(form.cleaned_data["twitter_url"], "https://www.twitter.com/testuser")
        self.assertEqual(form.cleaned_data["github_url"], "https://www.github.com/testuser")
        self.assertEqual(form.cleaned_data["personal_website"], "https://www.testuser.net")

        # Check bound data

        form_output = []

        for boundfield in form:
            form_output.append([boundfield.label, boundfield.data])

        expected_output = [
            ["first_name", "Test"],
            ["last_name", "User"],
            ["nickname", "Tester"],
            ["postal_address", "23 Test Avenue, Test Road, Testville, Testshire, TS3 3TY, UK"],
            ["phone_number", "080-1236-9874"],
            ["email_address", "testuser@email.com"],
            ["linkedin_url", "https://www.linkedin.com/testuser"],
            ["twitter_url", "https://www.twitter.com/testuser"],
            ["github_url", "https://www.github.com/testuser"],
            ["personal_website", "https://www.testuser.net"],
        ]

        self.assertEqual(form_output, expected_output)

    def test_custom_user_creation_form_when_empty(self):
        form = ContactForm()
        self.assertFalse(form.is_bound)
        # Should be an empty dictionary as validation is not carried out
        self.assertEqual(
            form.errors, {}
        )
        self.assertFalse(form.is_valid())
        with self.assertRaises(AttributeError):
            form.cleaned_data

    def test_custom_user_creation_form_when_partially_empty(self):
        form = ContactForm(
            {"nickname": "Tester", "email": "testuser@email.com"}
        )
        self.assertEqual(form.errors["first_name"], ["This field is required."])
        self.assertEqual(form.errors["last_name"], ["This field is required."])
        self.assertFalse(form.is_valid())

