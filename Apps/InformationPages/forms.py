from django import forms
from Apps.InformationPages.models import SendEmailClass

class SendEmailForm(forms.ModelForm):

    class Meta:
        model = SendEmailClass

        fields = [
            'name',
            'surname',
            'email',
            'description',
        ]

        fields = {
            'name': 'Nombre',
            'surname': 'Apellido',
            'email': 'Correo',
            'description': 'Descripción',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombres'}),
            'surname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellidos'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "usuario@example.com"}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escriba aquí...'}),
        }