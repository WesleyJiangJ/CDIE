from django.urls import path
from Apps.InformationPages.views import Index, About, Contact, Redirect

urlpatterns = [
    path('', Redirect, name='Redirect'),
    path('index/', Index, name='Index'),
    path('about/', About, name='About'),
    path('contact/', Contact.as_view(), name='Contact'),
]