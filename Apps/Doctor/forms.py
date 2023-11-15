from django import forms
from Apps.Doctor.models import AddUser, Patient, Doctor, Assistant, PatientMedicalHistory, UploadFile, Appointment, BudgetFields, Mouth

Sex = [
    ('0', 'Femenino'),
    ('1', 'Masculino'),
]

MaritalStatus = [
    ('0', 'Soltero'),
    ('1', 'Casado'),
]

Choose = [
    ('1', 'Si'),
    ('0', 'No'),
]

Experience = [
    ('0', 'Favorable'),
    ('1', 'Regular'),
    ('2', 'Desfavorable'),
]

Brush = [
    ('0', 'Duro'),
    ('1', 'Mediano'),
    ('2', 'Suave'),
    ('3', 'Extra Suave'),
]

Frecuency = [
    ('0', 'Una vez al dia'),
    ('1', 'Dos veces al dia'),
    ('2', 'Tres veces al dia'),
    ('3', 'Mas de tres veces al dia'),
]

Departments = [
    ('0', 'Atlántico Norte'),
    ('1', 'Atlántico Sur'),
    ('2', 'Boaco'),
    ('3', 'Carazo'),
    ('4', 'Chinandega'),
    ('5', 'Chontales'),
    ('6', 'Esteli'),
    ('7', 'Granada'),
    ('8', 'Jinotega'),
    ('9', 'León'),
    ('10', 'Madriz'),
    ('11', 'Managua'),
    ('12', 'Masaya'),
    ('13', 'Matagalpa'),
    ('14', 'Nueva Segovia'),
    ('15', 'Río San Juan'),
    ('16', 'Rivas'),
    ('17', 'Extranjero'),
]

# Odontogram
MOUTH_CHOICES = (
    ('sano', 'sano'),
    ('c1', 'c1'),
    ('c2', 'c2'),
    ('c3', 'c3'),
    ('c4', 'c4'),
    ('c5', 'c5'),
    ('r1', 'r1'),
    ('r2', 'r2'),
    ('r3', 'r3'),
    ('r4', 'r4'),
    ('r5', 'r5'),
    ('e', 'e'),
    ('N', 'N'),
    ('PL', 'PL'),
    ('p', 'p'),
    ('z', 'z'),
    ('d', 'd'),
    ('g', 'g'),
)



class FormularioUsuario(forms.ModelForm):

    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese su contraseña',
            'id': 'password1',
            'required': 'required',
        }
    ))

    password2 = forms.CharField(label='Contraseña 2', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese su contraseña',
            'id': 'password2',
            'required': 'required',
        }
    ))

    class Meta:
        model = AddUser
        # fields = '__all__'

        fields = ('email',)
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su correo electrónico'}),
        }

    """ Validación de Contraseña """

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('password didn"t match')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()
        return user


class AddPatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('FirstName', 'SecondName', 'FirstSurname', 'SecondSurname', 'Birthdate', 'Sex', 'Address',
                  'Origin', 'Phone', 'Email', 'Occupation', 'MaritalStatus', 'EmergencyCase', 'EmergencyNumber',)
        widgets = {
            'FirstName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escriba el primer nombre'}),
            'SecondName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escriba el segundo nombre'}),
            'FirstSurname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escriba el primer apellido'}),
            'SecondSurname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escriba el segundo apellido'}),
            'Birthdate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Sex': forms.RadioSelect(choices=Sex),
            'Address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Las Colinas'}),
            'Origin': forms.Select(attrs={'class': 'form-control'}, choices=Departments),
            'Phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '87654321'}),
            'Email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'user@example.com'}),
            'Occupation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escriba su ocupación'}),
            'MaritalStatus': forms.Select(attrs={'class': 'form-control'}, choices=MaritalStatus),
            'EmergencyCase': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de contacto'}),
            'EmergencyNumber': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número de contacto'}),
        }

class PatientMedicalHistoryForm(forms.ModelForm):
    class Meta:
        model = PatientMedicalHistory
        fields = ('Alergias', 'Patologicos', 'Farmacologicos', 'Hospitalizaciones', 'Quirurgico', 'Transfusiones', 'Radioterapia', 'Quimioterapia', 'Habitos', 'COVID', 'CantidadDosis', 'UltimaDosis', 'Observaciones', 'VisitaFrecuente', 'FechaUltimaVisita',
                  'HiloDental', 'Enjuague', 'Experiencia', 'TipoCepillo', 'FrecuenciaDeCepillado', 'FrecuenciaDeHilo', 'Otros', 'Periodoncia', 'Endodoncia', 'Exodoncia', 'ImplanteDental', 'Protesis', 'OperatoriaDental', 'CirugiaOral', 'Ortodoncia', 'Diagnostico',)
        widgets = {
            'Alergias': forms.RadioSelect(choices=Choose),
            'Patologicos': forms.RadioSelect(choices=Choose),
            'Farmacologicos': forms.RadioSelect(choices=Choose),
            'Hospitalizaciones': forms.RadioSelect(choices=Choose),
            'Quirurgico': forms.RadioSelect(choices=Choose),
            'Transfusiones': forms.RadioSelect(choices=Choose),
            'Radioterapia': forms.RadioSelect(choices=Choose),
            'Quimioterapia': forms.RadioSelect(choices=Choose),
            'Habitos': forms.RadioSelect(choices=Choose),
            'COVID': forms.RadioSelect(choices=Choose, attrs={'onchange': "showContent()"}),
            'CantidadDosis': forms.NumberInput(attrs={'class': 'form-control', 'value': '0'}),
            'UltimaDosis': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Observaciones': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escriba aqui...'}),
            'VisitaFrecuente': forms.RadioSelect(choices=Choose, attrs={'onchange': 'showContentFrecuency()'}),
            'FechaUltimaVisita': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'HiloDental': forms.RadioSelect(choices=Choose, attrs={'onchange': 'showFlossFrecuency()'}),
            'Enjuague': forms.RadioSelect(choices=Choose),
            'Experiencia': forms.RadioSelect(choices=Experience),
            'TipoCepillo': forms.RadioSelect(choices=Brush),
            'FrecuenciaDeCepillado': forms.Select(attrs={'class': 'form-control'}, choices=Frecuency),
            'FrecuenciaDeHilo': forms.Select(attrs={'class': 'form-control'}, choices=Frecuency),
            'Otros': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escriba aqui...'}),
            'Periodoncia': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'Endodoncia': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'Exodoncia': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'ImplanteDental': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'Protesis': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'OperatoriaDental': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'CirugiaOral': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'Ortodoncia': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'Diagnostico': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class UploadDocumentForm(forms.ModelForm):
    class Meta:
        model = UploadFile
        fields = ('File',)
        widgets = {
            'File': forms.FileInput(attrs={'class': 'form-control btn btn-primary', 'style': 'border-bottom-left-radius: 5px;', 'accept': 'application/pdf'})
        }

class AddDoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ('FirstName', 'SecondName', 'FirstSurname', 'SecondSurname', 'Birthdate', 'Sex', 'Address',
                  'Origin', 'Phone', 'Email', 'MaritalStatus',)
        widgets = {
            'FirstName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escriba el primer nombre'}),
            'SecondName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escriba el segundo nombre'}),
            'FirstSurname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escriba el primer apellido'}),
            'SecondSurname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escriba el segundo apellido'}),
            'Birthdate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Sex': forms.RadioSelect(choices=Sex),
            'Address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Las Colinas'}),
            'Origin': forms.Select(attrs={'class': 'form-control'}, choices=Departments),
            'Phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '87654321'}),
            'Email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'user@example.com'}),
            'MaritalStatus': forms.Select(attrs={'class': 'form-control'}, choices=MaritalStatus),
        }

class AddAssistantForm(forms.ModelForm):
    class Meta:
        model = Assistant
        fields = ('FirstName', 'SecondName', 'FirstSurname', 'SecondSurname', 'Birthdate', 'Sex', 'Address',
                  'Origin', 'Phone', 'Email', 'MaritalStatus',)
        widgets = {
            'FirstName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escriba el primer nombre'}),
            'SecondName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escriba el segundo nombre'}),
            'FirstSurname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escriba el primer apellido'}),
            'SecondSurname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escriba el segundo apellido'}),
            'Birthdate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Sex': forms.RadioSelect(choices=Sex),
            'Address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Las Colinas'}),
            'Origin': forms.Select(attrs={'class': 'form-control'}, choices=Departments),
            'Phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '87654321'}),
            'Email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'user@example.com'}),
            'MaritalStatus': forms.Select(attrs={'class': 'form-control'}, choices=MaritalStatus),
        }

class AddAppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('Description', 'Date',)
        widgets = {
            'Description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escriba aquí...'}),
            'Date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }

class BudgetFieldForm(forms.ModelForm):
    class Meta:
        model = BudgetFields
        fields = ('Quantity', 'Treatment', 'Cost',)
        widgets = {
            'Quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0', 'onkeyup':'calcular()', 'onkeypress':"return event.charCode>=48 && event.charCode<=57"}),
            'Treatment': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tratamiento a realizar'}),
            'Cost': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'C$0.00', 'onkeyup':'calcular()', 'onkeypress':"return event.charCode>=48 && event.charCode<=57"}),
        }

# Odontogram
class T11Form(forms.ModelForm):
    t_11 = forms.MultipleChoiceField(
        choices=MOUTH_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
        #label='',
    )

    class Meta:
        model = Mouth
        fields = ['t_11', ]


class T12Form(forms.ModelForm):
    t_12 = forms.MultipleChoiceField(
        choices=MOUTH_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
        #label='',
    )

    class Meta:
        model = Mouth
        fields = ['t_12', ]


class T13Form(forms.ModelForm):
    t_13 = forms.MultipleChoiceField(
        choices=MOUTH_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
        #label='',
    )

    class Meta:
        model = Mouth
        fields = ['t_13', ]


class T14Form(forms.ModelForm):
    t_14 = forms.MultipleChoiceField(
        choices=MOUTH_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
        #label='',
    )

    class Meta:
        model = Mouth
        fields = ['t_14', ]


class T15Form(forms.ModelForm):
    t_15 = forms.MultipleChoiceField(
        choices=MOUTH_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
        #label='',
    )

    class Meta:
        model = Mouth
        fields = ['t_15', ]


class T16Form(forms.ModelForm):
    t_16 = forms.MultipleChoiceField(
        choices=MOUTH_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
        #label='',
    )

    class Meta:
        model = Mouth
        fields = ['t_16', ]


class T17Form(forms.ModelForm):
    t_17 = forms.MultipleChoiceField(
        choices=MOUTH_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
        #label='',
    )

    class Meta:
        model = Mouth
        fields = ['t_17', ]


class T18Form(forms.ModelForm):
    t_18 = forms.MultipleChoiceField(
        choices=MOUTH_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
        #label='',
    )

    class Meta:
        model = Mouth
        fields = ['t_18', ]


class T21Form(forms.ModelForm):
    t_21 = forms.MultipleChoiceField(
        choices=MOUTH_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
        #label='',
    )

    class Meta:
        model = Mouth
        fields = ['t_21', ]


class T22Form(forms.ModelForm):
    t_22 = forms.MultipleChoiceField(
        choices=MOUTH_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
        #label='',
    )

    class Meta:
        model = Mouth
        fields = ['t_22', ]


class T23Form(forms.ModelForm):
    t_23 = forms.MultipleChoiceField(
        choices=MOUTH_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
        #label='',
    )

    class Meta:
        model = Mouth
        fields = ['t_23', ]


class T24Form(forms.ModelForm):
    t_24 = forms.MultipleChoiceField(
        choices=MOUTH_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
        #label='',
    )

    class Meta:
        model = Mouth
        fields = ['t_24', ]


class T25Form(forms.ModelForm):
    t_25 = forms.MultipleChoiceField(
        choices=MOUTH_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
        #label='',
    )

    class Meta:
        model = Mouth
        fields = ['t_25', ]


class T26Form(forms.ModelForm):
    t_26 = forms.MultipleChoiceField(
        choices=MOUTH_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
        #label='',
    )

    class Meta:
        model = Mouth
        fields = ['t_26', ]


class T27Form(forms.ModelForm):
    t_27 = forms.MultipleChoiceField(
        choices=MOUTH_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
        #label='',
    )

    class Meta:
        model = Mouth
        fields = ['t_27', ]


class T28Form(forms.ModelForm):
    t_28 = forms.MultipleChoiceField(
        choices=MOUTH_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
        #label='',
    )

    class Meta:
        model = Mouth
        fields = ['t_28', ]


class T31Form(forms.ModelForm):
    t_31 = forms.MultipleChoiceField(
        choices=MOUTH_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
        #label='',
    )

    class Meta:
        model = Mouth
        fields = ['t_31', ]


class T32Form(forms.ModelForm):
    t_32 = forms.MultipleChoiceField(
        choices=MOUTH_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
        #label='',
    )

    class Meta:
        model = Mouth
        fields = ['t_32', ]


class T33Form(forms.ModelForm):
    t_33 = forms.MultipleChoiceField(
        choices=MOUTH_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
        #label='',
    )

    class Meta:
        model = Mouth
        fields = ['t_33', ]


class T34Form(forms.ModelForm):
    t_34 = forms.MultipleChoiceField(
        choices=MOUTH_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
        #label='',
    )

    class Meta:
        model = Mouth
        fields = ['t_34', ]


class T35Form(forms.ModelForm):
    t_35 = forms.MultipleChoiceField(
        choices=MOUTH_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
        #label='',
    )

    class Meta:
        model = Mouth
        fields = ['t_35', ]


class T36Form(forms.ModelForm):
    t_36 = forms.MultipleChoiceField(
        choices=MOUTH_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
        #label='',
    )

    class Meta:
        model = Mouth
        fields = ['t_36', ]


class T37Form(forms.ModelForm):
    t_37 = forms.MultipleChoiceField(
        choices=MOUTH_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
        #label='',
    )

    class Meta:
        model = Mouth
        fields = ['t_37', ]


class T38Form(forms.ModelForm):
    t_38 = forms.MultipleChoiceField(
        choices=MOUTH_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
        #label='',
    )

    class Meta:
        model = Mouth
        fields = ['t_38', ]


class T41Form(forms.ModelForm):
    t_41 = forms.MultipleChoiceField(
        choices=MOUTH_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
        #label='',
    )

    class Meta:
        model = Mouth
        fields = ['t_41', ]


class T42Form(forms.ModelForm):
    t_42 = forms.MultipleChoiceField(
        choices=MOUTH_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
        #label='',
    )

    class Meta:
        model = Mouth
        fields = ['t_42', ]


class T43Form(forms.ModelForm):
    t_43 = forms.MultipleChoiceField(
        choices=MOUTH_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
        #label='',
    )

    class Meta:
        model = Mouth
        fields = ['t_43', ]


class T44Form(forms.ModelForm):
    t_44 = forms.MultipleChoiceField(
        choices=MOUTH_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
        #label='',
    )

    class Meta:
        model = Mouth
        fields = ['t_44', ]


class T45Form(forms.ModelForm):
    t_45 = forms.MultipleChoiceField(
        choices=MOUTH_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
        #label='',
    )

    class Meta:
        model = Mouth
        fields = ['t_45', ]


class T46Form(forms.ModelForm):
    t_46 = forms.MultipleChoiceField(
        choices=MOUTH_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
        #label='',
    )

    class Meta:
        model = Mouth
        fields = ['t_46', ]


class T47Form(forms.ModelForm):
    t_47 = forms.MultipleChoiceField(
        choices=MOUTH_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
        #label='',
    )

    class Meta:
        model = Mouth
        fields = ['t_47', ]


class T48Form(forms.ModelForm):
    t_48 = forms.MultipleChoiceField(
        choices=MOUTH_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
        #label='',
    )

    class Meta:
        model = Mouth
        fields = ['t_48', ]


class T51Form(forms.ModelForm):
    t_51 = forms.MultipleChoiceField(
        choices=MOUTH_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
        #label='',
    )

    class Meta:
        model = Mouth
        fields = ['t_51', ]


class T52Form(forms.ModelForm):
    t_52 = forms.MultipleChoiceField(
        choices=MOUTH_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
        #label='',
    )

    class Meta:
        model = Mouth
        fields = ['t_52', ]


class T53Form(forms.ModelForm):
    t_53 = forms.MultipleChoiceField(
        choices=MOUTH_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
        #label='',
    )

    class Meta:
        model = Mouth
        fields = ['t_53', ]


class T54Form(forms.ModelForm):
    t_54 = forms.MultipleChoiceField(
        choices=MOUTH_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
        #label='',
    )

    class Meta:
        model = Mouth
        fields = ['t_54', ]


class T55Form(forms.ModelForm):
    t_55 = forms.MultipleChoiceField(
        choices=MOUTH_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
        #label='',
    )

    class Meta:
        model = Mouth
        fields = ['t_55', ]


class T61Form(forms.ModelForm):
    t_61 = forms.MultipleChoiceField(
        choices=MOUTH_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
        #label='',
    )

    class Meta:
        model = Mouth
        fields = ['t_61', ]


class T62Form(forms.ModelForm):
    t_62 = forms.MultipleChoiceField(
        choices=MOUTH_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
        #label='',
    )

    class Meta:
        model = Mouth
        fields = ['t_62', ]


class T63Form(forms.ModelForm):
    t_63 = forms.MultipleChoiceField(
        choices=MOUTH_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
        #label='',
    )

    class Meta:
        model = Mouth
        fields = ['t_63', ]


class T64Form(forms.ModelForm):
    t_64 = forms.MultipleChoiceField(
        choices=MOUTH_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
        #label='',
    )

    class Meta:
        model = Mouth
        fields = ['t_64', ]


class T65Form(forms.ModelForm):
    t_65 = forms.MultipleChoiceField(
        choices=MOUTH_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
        #label='',
    )

    class Meta:
        model = Mouth
        fields = ['t_65', ]


class T71Form(forms.ModelForm):
    t_71 = forms.MultipleChoiceField(
        choices=MOUTH_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
        #label='',
    )

    class Meta:
        model = Mouth
        fields = ['t_71', ]


class T72Form(forms.ModelForm):
    t_72 = forms.MultipleChoiceField(
        choices=MOUTH_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
        #label='',
    )

    class Meta:
        model = Mouth
        fields = ['t_72', ]


class T73Form(forms.ModelForm):
    t_73 = forms.MultipleChoiceField(
        choices=MOUTH_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
        #label='',
    )

    class Meta:
        model = Mouth
        fields = ['t_73', ]


class T74Form(forms.ModelForm):
    t_74 = forms.MultipleChoiceField(
        choices=MOUTH_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
        #label='',
    )

    class Meta:
        model = Mouth
        fields = ['t_74', ]


class T75Form(forms.ModelForm):
    t_75 = forms.MultipleChoiceField(
        choices=MOUTH_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
        #label='',
    )

    class Meta:
        model = Mouth
        fields = ['t_75', ]


class T81Form(forms.ModelForm):
    t_81 = forms.MultipleChoiceField(
        choices=MOUTH_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
        #label='',
    )

    class Meta:
        model = Mouth
        fields = ['t_81', ]


class T82Form(forms.ModelForm):
    t_82 = forms.MultipleChoiceField(
        choices=MOUTH_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
        #label='',
    )

    class Meta:
        model = Mouth
        fields = ['t_82', ]


class T83Form(forms.ModelForm):
    t_83 = forms.MultipleChoiceField(
        choices=MOUTH_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
        #label='',
    )

    class Meta:
        model = Mouth
        fields = ['t_83', ]


class T84Form(forms.ModelForm):
    t_84 = forms.MultipleChoiceField(
        choices=MOUTH_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
        #label='',
    )

    class Meta:
        model = Mouth
        fields = ['t_84', ]


class T85Form(forms.ModelForm):
    t_85 = forms.MultipleChoiceField(
        choices=MOUTH_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
        #label='',
    )

    class Meta:
        model = Mouth
        fields = ['t_85', ]
# Odontogram END