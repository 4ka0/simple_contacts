from django.urls import path

from .views import (
    ContactListView,
    ContactCreateView,
    ContactUpdateView,
    ContactDeleteView,
    ContactDetailView
)


urlpatterns = [
    path('', ContactListView.as_view(), name='contact_list'),
    path('new/', ContactCreateView.as_view(), name='contact_new'),
    path('<int:pk>/edit/', ContactUpdateView.as_view(), name='contact_edit'),
    path('<int:pk>/delete/', ContactDeleteView.as_view(), name='contact_delete'),
    path('<int:pk>/', ContactDetailView.as_view(), name='contact_detail'),
]