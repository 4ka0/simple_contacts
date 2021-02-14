from django.urls import path

from . import views


urlpatterns = [
    path('', views.contact_list, name='contact_list'),
    path('new/', views.contact_new, name='contact_new'),
    path('<int:pk>/', views.contact_detail, name='contact_detail'),
    path('<int:pk>/edit/', views.contact_edit, name='contact_edit'),
    path('<int:pk>/delete/', views.contact_delete, name='contact_delete'),
]