from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from .models import Contact
from .forms import ContactForm


def contact_list(request):
    contacts = Contact.objects.order_by('first_name')
    return render(request, 'contact_list.html', {'contacts': contacts})


def contact_alphabet(request, letters):

    if letters == 'A-E':
        contacts = Contact.objects.filter(
            Q(first_name__startswith='A') |
            Q(first_name__startswith='B') |
            Q(first_name__startswith='C') |
            Q(first_name__startswith='D') |
            Q(first_name__startswith='E')
        )

    elif letters == 'F-J':
        contacts = Contact.objects.filter(
            Q(first_name__startswith='F') |
            Q(first_name__startswith='G') |
            Q(first_name__startswith='H') |
            Q(first_name__startswith='I') |
            Q(first_name__startswith='J')
        )

    elif letters == 'K-O':
        contacts = Contact.objects.filter(
            Q(first_name__startswith='K') |
            Q(first_name__startswith='L') |
            Q(first_name__startswith='M') |
            Q(first_name__startswith='N') |
            Q(first_name__startswith='O')
        )

    elif letters == 'P-T':
        contacts = Contact.objects.filter(
            Q(first_name__startswith='P') |
            Q(first_name__startswith='Q') |
            Q(first_name__startswith='R') |
            Q(first_name__startswith='S') |
            Q(first_name__startswith='T')
        )

    else:
        contacts = Contact.objects.filter(
            Q(first_name__startswith='U') |
            Q(first_name__startswith='V') |
            Q(first_name__startswith='W') |
            Q(first_name__startswith='X') |
            Q(first_name__startswith='Z') |
            Q(first_name__startswith='Y')
        )

    contacts = contacts.order_by('first_name')

    return render(request, 'contact_list.html', {'contacts': contacts})


def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'contact_detail.html', {'contact': contact})


def contact_new(request):

    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid:
            contact = form.save()
            return redirect('contact_detail', pk=contact.pk)

    else:
        form = ContactForm()
    return render(request, 'contact_new.html', {'form': form})


def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)

    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')

    return render(request, 'contact_delete.html', {'contact': contact})


def contact_edit(request, pk):
    contact = get_object_or_404(Contact, pk=pk)

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=contact)
        if form.is_valid():
            contact = form.save(commit=False)  # Provides unsaved model object

            # Delete associated thumbnail if profile picture has been cleared
            if not form.cleaned_data.get('profile_picture'):
                contact.thumbnail.delete()

            contact.last_modified_on = timezone.now()
            contact.save()
            return redirect('contact_detail', pk=contact.pk)

    else:
        form = ContactForm(instance=contact)
    return render(request, 'contact_edit.html', {'form': form})
