from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy

from .models import Contact


class ContactListView(ListView):
    model = Contact
    template_name = 'contact_list.html'


class ContactCreateView(CreateView):
    model = Contact
    fields = (
        'first_name',
        'last_name',
        'nickname',
        'postal_address',
        'phone_number',
        'email_address',
        'linkedin_url',
        'twitter_url',
        'personal_website'
    )
    template_name = 'contact_new.html'
    success_url = reverse_lazy('contact_list')


class ContactUpdateView(UpdateView):
    model = Contact
    fields = (
        'first_name',
        'last_name',
        'nickname',
        'postal_address',
        'phone_number',
        'email_address',
        'linkedin_url',
        'twitter_url',
        'personal_website'
    )
    template_name = 'contact_edit.html'
    # success_url = reverse_lazy('contact_list')


class ContactDeleteView(DeleteView):
    model = Contact
    template_name = 'contact_delete.html'
    success_url = reverse_lazy('contact_list')


class ContactDetailView(DetailView):
    model = Contact
    template_name = 'contact_detail.html'