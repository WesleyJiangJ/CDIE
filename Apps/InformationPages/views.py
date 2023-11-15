from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from Apps.InformationPages.models import SendEmailClass
from Apps.InformationPages.forms import SendEmailForm

# Create your views here.
def Index(request):
    return render(request, 'index.html')

def Redirect(request):
    return redirect('Index')

def About(request):
    return render(request, 'about.html')

class Contact(CreateView):
    model = SendEmailClass
    form_class = SendEmailForm
    template_name = 'contact.html'
    success_url = reverse_lazy('SendEmail')