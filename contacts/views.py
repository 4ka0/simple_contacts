from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404

from .models import Contact
from .forms import ContactForm


def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contact_list.html', {'contacts': contacts})


def contact_alphabet(request, letter):
    contacts = Contact.objects.filter(first_name__istartswith=letter)
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


def contact_edit(request, pk):
    contact = get_object_or_404(Contact, pk=pk)

    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES, instance=contact)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.last_modified_on = timezone.now()
            contact.save()
            return redirect('contact_detail', pk=contact.pk)

    else:
        form = ContactForm(instance=contact)
    return render(request, 'contact_edit.html', {'form': form})


def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)

    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')

    return render(request, 'contact_delete.html', {'contact': contact})