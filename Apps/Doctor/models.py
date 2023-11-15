from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from datetime import date

# Create your models here.
# Patient


class Patient(models.Model):
    FirstName = models.TextField(max_length=50)
    SecondName = models.TextField(max_length=50)
    FirstSurname = models.TextField(max_length=50)
    SecondSurname = models.TextField(max_length=50)
    Birthdate = models.DateField()
    Sex = models.CharField(max_length=1)
    Address = models.TextField()
    Origin = models.CharField(max_length=2)
    Phone = models.TextField(max_length=8)
    Email = models.EmailField(max_length=254)
    Occupation = models.TextField(max_length=50)
    MaritalStatus = models.CharField(max_length=1)
    EmergencyCase = models.TextField(max_length=50)
    EmergencyNumber = models.TextField(max_length=8)
    Status = models.BooleanField(default=True)

    def __unicode__(self):
        return "FirstName: {0}, SecondName: {1}, FirstSurname: {2}, SecondSurname: {3}".format(self.FirstName, self.SecondName, self.FirstSurname, self.SecondSurname)


class UploadFile(models.Model):
    idPatient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, null=False)
    File = models.FileField()


class PatientMedicalHistory(models.Model):
    idPatient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, null=False)
    Alergias = models.CharField(max_length=1)
    Patologicos = models.CharField(max_length=1)
    Farmacologicos = models.CharField(max_length=1)
    Hospitalizaciones = models.CharField(max_length=1)
    Quirurgico = models.CharField(max_length=1)
    Transfusiones = models.CharField(max_length=1)
    Radioterapia = models.CharField(max_length=1)
    Quimioterapia = models.CharField(max_length=1)
    Habitos = models.CharField(max_length=1)
    COVID = models.CharField(max_length=1)
    CantidadDosis = models.IntegerField(null=True, blank=True)
    UltimaDosis = models.DateField(blank=True, null=True)
    Observaciones = models.TextField(blank=True, null=True)

    VisitaFrecuente = models.CharField(max_length=1)
    FechaUltimaVisita = models.DateField(blank=True, null=True)
    HiloDental = models.CharField(max_length=1)
    Enjuague = models.CharField(max_length=1)
    Experiencia = models.CharField(max_length=1, blank=True, null=True)
    TipoCepillo = models.CharField(max_length=1)
    FrecuenciaDeCepillado = models.CharField(max_length=1)
    FrecuenciaDeHilo = models.CharField(max_length=1, null=True, blank=True)
    Otros = models.TextField(null=True, blank=True)

    Periodoncia = models.BooleanField(default=False)
    Endodoncia = models.BooleanField(default=False)
    Exodoncia = models.BooleanField(default=False)
    ImplanteDental = models.BooleanField(default=False)
    Protesis = models.BooleanField(default=False)
    OperatoriaDental = models.BooleanField(default=False)
    CirugiaOral = models.BooleanField(default=False)
    Ortodoncia = models.BooleanField(default=False)
    Diagnostico = models.BooleanField(default=False)


class Doctor(models.Model):
    FirstName = models.TextField(max_length=50)
    SecondName = models.TextField(max_length=50)
    FirstSurname = models.TextField(max_length=50)
    SecondSurname = models.TextField(max_length=50)
    Birthdate = models.DateField()
    Sex = models.CharField(max_length=1)
    Address = models.TextField()
    Origin = models.CharField(max_length=2)
    Phone = models.TextField(max_length=8)
    Email = models.EmailField(max_length=254)
    MaritalStatus = models.CharField(max_length=1)
    Status = models.BooleanField(default=True)


class Assistant(models.Model):
    FirstName = models.TextField(max_length=50)
    SecondName = models.TextField(max_length=50)
    FirstSurname = models.TextField(max_length=50)
    SecondSurname = models.TextField(max_length=50)
    Birthdate = models.DateField()
    Sex = models.CharField(max_length=1)
    Address = models.TextField()
    Origin = models.CharField(max_length=2)
    Phone = models.TextField(max_length=8)
    Email = models.EmailField(max_length=254)
    MaritalStatus = models.CharField(max_length=1)
    Status = models.BooleanField(default=True)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Email is Required')

        usuario = self.model(
            email=self.normalize_email(email),
        )

        usuario.set_password(password)
        usuario.save()

        return usuario

    def create_superuser(self, email, password):
        usuario = self.create_user(
            email,
            password=password,
        )

        usuario.usuario_administrador = True
        usuario.save()
        return usuario


class AddUser(AbstractBaseUser):
    email = models.EmailField('Correo', unique=True, max_length=254)
    idPatient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    idDoctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)
    idPersonal = models.ForeignKey(Assistant, on_delete=models.CASCADE, null=True)

    usuario_activo = models.BooleanField(default=True)
    usuario_administrador = models.BooleanField(default=False)

    object = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'Usuario: {self.email}'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.usuario_administrador


class Appointment(models.Model):
    class Meta:
        ordering = ['Date']
    idPatient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, null=False)
    idDoctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=False)
    Description = models.TextField()
    Date = models.DateTimeField()
    Status = models.CharField(max_length=1, default='1')


class MainBudget(models.Model):
    idPatient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, null=False)
    idDoctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=False)
    Date = models.DateField(default=date.today)
    State = models.CharField(max_length=1, default = '1')

    # def __unicode__(self):
    #     return "Date: {0}".format(self.Date)


class BudgetFields(models.Model):
    idMainBudget = models.ForeignKey(MainBudget, on_delete=models.CASCADE, null=False)
    Quantity = models.PositiveIntegerField()
    Treatment = models.TextField()
    Cost = models.DecimalField(max_digits=6, decimal_places=2)

    # def __unicode__(self):
    #     return "Quantity: {0}, Treatment: {1}, Cost: {2}".format(self.Quantity, self.Treatment, self.Cost)


class PaymentControl(models.Model):
    idMainBudget = models.ForeignKey(MainBudget, on_delete=models.CASCADE, null=False)
    Date = models.DateField(default=date.today)
    Credit = models.DecimalField(max_digits=6, decimal_places=2)
    Done = models.BooleanField(default=False)

    # def __unicode__(self):
    #     return "Date: {0}, Credit: {1}, Balance: {2}".format(self.Date, self.Credit, self.Balance)


class PaymentDone(models.Model):
    idMainBudget = models.ForeignKey(BudgetFields, on_delete=models.CASCADE, null=False)
    Date = models.DateField(default=date.today)
    Paid = models.DecimalField(max_digits=6, decimal_places=2, null=False)

class Mouth(models.Model):
    """
    Odontogram, the fact that teeth were distributed
    inside a mouth model, and not as single instances
    in a model 'tooth' was to avoid excesive database
    hits when displaying the main odontogram in patient
    general information
    """
    idPatient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=False)
    state = models.CharField(max_length=1, default='1')
    date = models.DateTimeField(default=date.today, editable=False)
    t_11 = models.CharField(max_length=90, default='sano')
    t_12 = models.CharField(max_length=90, default='sano')
    t_13 = models.CharField(max_length=90, default='sano')
    t_14 = models.CharField(max_length=90, default='sano')
    t_15 = models.CharField(max_length=90, default='sano')
    t_16 = models.CharField(max_length=90, default='sano')
    t_17 = models.CharField(max_length=90, default='sano')
    t_18 = models.CharField(max_length=90, default='sano')
    t_21 = models.CharField(max_length=90, default='sano')
    t_22 = models.CharField(max_length=90, default='sano')
    t_23 = models.CharField(max_length=90, default='sano')
    t_24 = models.CharField(max_length=90, default='sano')
    t_25 = models.CharField(max_length=90, default='sano')
    t_26 = models.CharField(max_length=90, default='sano')
    t_27 = models.CharField(max_length=90, default='sano')
    t_28 = models.CharField(max_length=90, default='sano')
    t_31 = models.CharField(max_length=90, default='sano')
    t_32 = models.CharField(max_length=90, default='sano')
    t_33 = models.CharField(max_length=90, default='sano')
    t_34 = models.CharField(max_length=90, default='sano')
    t_35 = models.CharField(max_length=90, default='sano')
    t_36 = models.CharField(max_length=90, default='sano')
    t_37 = models.CharField(max_length=90, default='sano')
    t_38 = models.CharField(max_length=90, default='sano')
    t_41 = models.CharField(max_length=90, default='sano')
    t_42 = models.CharField(max_length=90, default='sano')
    t_43 = models.CharField(max_length=90, default='sano')
    t_44 = models.CharField(max_length=90, default='sano')
    t_45 = models.CharField(max_length=90, default='sano')
    t_46 = models.CharField(max_length=90, default='sano')
    t_47 = models.CharField(max_length=90, default='sano')
    t_48 = models.CharField(max_length=90, default='sano')
    t_51 = models.CharField(max_length=90, default='sano')
    t_52 = models.CharField(max_length=90, default='sano')
    t_53 = models.CharField(max_length=90, default='sano')
    t_54 = models.CharField(max_length=90, default='sano')
    t_55 = models.CharField(max_length=90, default='sano')
    t_61 = models.CharField(max_length=90, default='sano')
    t_62 = models.CharField(max_length=90, default='sano')
    t_63 = models.CharField(max_length=90, default='sano')
    t_64 = models.CharField(max_length=90, default='sano')
    t_65 = models.CharField(max_length=90, default='sano')
    t_71 = models.CharField(max_length=90, default='sano')
    t_72 = models.CharField(max_length=90, default='sano')
    t_73 = models.CharField(max_length=90, default='sano')
    t_74 = models.CharField(max_length=90, default='sano')
    t_75 = models.CharField(max_length=90, default='sano')
    t_81 = models.CharField(max_length=90, default='sano')
    t_82 = models.CharField(max_length=90, default='sano')
    t_83 = models.CharField(max_length=90, default='sano')
    t_84 = models.CharField(max_length=90, default='sano')
    t_85 = models.CharField(max_length=90, default='sano')