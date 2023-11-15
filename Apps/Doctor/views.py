import os
import json

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy

from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView, TemplateView
from Apps.Doctor.models import AddUser, Patient, PatientMedicalHistory, UploadFile, Doctor, Assistant, Appointment, MainBudget, BudgetFields, PaymentControl, PaymentDone, Mouth
from Apps.Doctor.forms import AddPatientForm, PatientMedicalHistoryForm, PatientMedicalHistoryForm, UploadDocumentForm, AddDoctorForm, AddAssistantForm, AddAppointmentForm

from django.contrib.auth.hashers import make_password

from django.views.generic.edit import FormMixin

from . import forms

from django.contrib import messages

class DoctorIndex(TemplateView):
    template_name = "dIndex.html"

    def get_queryset(self):
        appointment = Appointment.objects.all()
        patient = Patient.objects.all()
        paymentControl = PaymentControl.objects.all()
        return appointment, patient, paymentControl

    def get(self, request, *args, **kwargs):
        if is_ajax(request=request):
            appointment, patient, paymentControl = self.get_queryset()
            List = []
            for info in appointment:
                data = {}
                data['id'] = info.id
                data['date'] = info.Date.month, info.Date.year
                data['state'] = info.Status
                data['idDoctorAppointment'] = info.idDoctor_id
                List.append(data)

            for info in patient:
                data = {}
                data['Patient'] = info.id
                data['PatientState'] = info.Status
                List.append(data)

            for info in paymentControl:
                data = {}
                data['PaymentControl'] = info.id
                data['PaymentState'] = info.Done
                List.append(data)
            data = json.dumps(List)
            return HttpResponse(data, 'application/json')
        else:
            return render(request, self.template_name)


def DoctorAddPatient(request):
    return render(request, 'dAddPatient.html')


class RegistrarUsuario(CreateView):
    model = Patient
    form_class = AddPatientForm
    second_form_class = PatientMedicalHistoryForm
    template_name = 'dAddPatient.html'
    success_url = reverse_lazy('DoctorPatient')

    def get_context_data(self, **kwargs):
        context = super(RegistrarUsuario, self).get_context_data(**kwargs)

        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)

        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)

        if form.is_valid() and form2.is_valid():
            try:
                solicitud = form.save(commit=False)
                # solicitud.PatientMedicalHistory = form2.save()
                solicitud.save()
                Email = form['Email'].value()
                Username = (form['FirstName'].value() +
                            form['FirstSurname'].value())
                Password = make_password(Username.lower())
                idPatient = (Patient.objects.last()).id
                User = AddUser(email=Email, password=Password,
                            idPatient_id=idPatient)
                User.save()
                messages.success(request, 'Paciente agregado')

                Alergias = form2['Alergias'].value()
                Patologicos = form2['Patologicos'].value()
                Farmacologicos = form2['Farmacologicos'].value()
                Hospitalizaciones = form2['Hospitalizaciones'].value()
                Quirurgico = form2['Quirurgico'].value()
                Transfusiones = form2['Transfusiones'].value()
                Radioterapia = form2['Radioterapia'].value()
                Quimioterapia = form2['Quimioterapia'].value()
                Habitos = form2['Habitos'].value()
                COVID = form2['COVID'].value()
                CantidadDosis = form2['CantidadDosis'].value()
                UltimaDosis = form2['UltimaDosis'].value()
                Observaciones = form2['Observaciones'].value()
                VisitaFrecuente = form2['VisitaFrecuente'].value()
                FechaUltimaVisita = form2['FechaUltimaVisita'].value()
                HiloDental = form2['HiloDental'].value()
                Enjuague = form2['Enjuague'].value()
                Experiencia = form2['Experiencia'].value()
                TipoCepillo = form2['TipoCepillo'].value()
                FrecuenciaDeCepillado = form2['FrecuenciaDeCepillado'].value()
                FrecuenciaDeHilo = form2['FrecuenciaDeHilo'].value()
                Otros = form2['Otros'].value()
                Periodoncia = form2['Periodoncia'].value()
                Endodoncia = form2['Endodoncia'].value()
                Exodoncia = form2['Exodoncia'].value()
                ImplanteDental = form2['ImplanteDental'].value()
                Protesis = form2['Protesis'].value()
                OperatoriaDental = form2['OperatoriaDental'].value()
                CirugiaOral = form2['CirugiaOral'].value()
                Ortodoncia = form2['Ortodoncia'].value()
                Diagnostico = form2['Diagnostico'].value()

                if UltimaDosis == "":
                    UltimaDosis = '0001-01-01'

                if FechaUltimaVisita == "":
                    FechaUltimaVisita = '0001-01-01'

                if HiloDental == '0':
                    FrecuenciaDeHilo = ""

                if VisitaFrecuente == '0':
                    FechaUltimaVisita = '0001-01-01'
                    Experiencia = ""

                if COVID == '0':
                    CantidadDosis = 0
                    UltimaDosis = '0001-01-01'

                Patients = PatientMedicalHistory(Alergias=Alergias, Patologicos=Patologicos, Farmacologicos=Farmacologicos, Hospitalizaciones=Hospitalizaciones, Quirurgico=Quirurgico, Transfusiones=Transfusiones, Radioterapia=Radioterapia, Quimioterapia=Quimioterapia, Habitos=Habitos, COVID=COVID, CantidadDosis=CantidadDosis, UltimaDosis=UltimaDosis, Observaciones=Observaciones, VisitaFrecuente=VisitaFrecuente, FechaUltimaVisita=FechaUltimaVisita,
                                                HiloDental=HiloDental, Enjuague=Enjuague, Experiencia=Experiencia, TipoCepillo=TipoCepillo, FrecuenciaDeCepillado=FrecuenciaDeCepillado, FrecuenciaDeHilo=FrecuenciaDeHilo, Otros=Otros, Periodoncia=Periodoncia, Endodoncia=Endodoncia, Exodoncia=Exodoncia, ImplanteDental=ImplanteDental, Protesis=Protesis, OperatoriaDental=OperatoriaDental, CirugiaOral=CirugiaOral, Ortodoncia=Ortodoncia, Diagnostico=Diagnostico, idPatient_id=idPatient)

                Patients.save()

                return HttpResponseRedirect(self.get_success_url())
            except:
                Patient.objects.filter(id=idPatient).delete()
                PatientMedicalHistory.objects.filter(idPatient_id=idPatient).delete()
                messages.error(request, 'Correo ya existente')
                return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

class PatientList(TemplateView):
    model = Patient
    template_name = "dPatientList.html"

    def get_queryset(self):
        return self.model.objects.all()

    def get(self, request, *args, **kwargs):
        if is_ajax(request=request):
            patientList = []
            for patient in self.get_queryset():
                data_patient = {}
                data_patient['id'] = patient.id
                data_patient['Fullname'] = patient.FirstName + " " + patient.SecondName + \
                    " " + patient.FirstSurname + " " + patient.SecondSurname
                data_patient['Phone'] = patient.Phone
                data_patient['Status'] = patient.Status
                patientList.append(data_patient)
                data = json.dumps(patientList)
            return HttpResponse(data, 'application/json')
        else:
            return render(request, self.template_name)


class PatientUpdate(UpdateView):
    model = Patient
    second_model = PatientMedicalHistory
    template_name = 'dAddPatient.html'
    form_class = AddPatientForm
    second_form_class = PatientMedicalHistoryForm

    # success_url = reverse_lazy('DoctorPatient')

    def get_context_data(self, **kwargs):
        context = super(PatientUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        solicitud = self.model.objects.get(id=pk)

        persona = self.second_model.objects.get(id=solicitud.id)

        if 'form' not in context:
            context['form'] = self.form_class()

        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=persona)

        context['id'] = pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_solicitud = kwargs['pk']

        solicitud = self.model.objects.get(id=id_solicitud)
        persona = self.second_model.objects.get(id=solicitud.id)

        # print("")
        # print("Persona es: ", persona.id)
        # print("")
        form = self.form_class(request.POST, instance=solicitud)
        form2 = self.second_form_class(request.POST, instance=persona)

        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()

            mainbudget = MainBudget.objects.filter(idPatient_id = id_solicitud)
            # print(mainbudget)
            paymentcontrol = PaymentControl.objects.all()

            # Check if there are Payments without be paid
            PaymentCheck = ''
            for i in mainbudget:
                if i.State == '0':
                    for j in paymentcontrol:
                        if i.id == j.idMainBudget_id:
                            if j.Done == False:
                                PaymentCheck = '1'

            if 'Status' in request.POST:
                obj = form.save(commit=False)
                if obj.Status == True:
                    if PaymentCheck != '1':
                        obj.Status = False
                        Appointment.objects.filter(idPatient_id = id_solicitud).update(Status='0')
                        messages.info(request, 'El paciente ha sido dado de baja')
                    else:
                        messages.error(request, 'No puede darse de baja, hay controles de pagos activos')
                else:
                    obj.Status = True
                    messages.info(request, 'El paciente ha sido dado de alta')
                obj.save()

            return redirect('PatientDetailView', persona.id)
        else:
            return redirect('PatientDetailView', persona.id)


class PatientDetailView(FormMixin, DetailView):
    model = Patient
    model2 = UploadFile
    template_name = 'dPatientDetail.html'
    form_class = UploadDocumentForm

    def get_success_url(self):
        # print('Get Success URL')
        return reverse('PatientDetailView', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        # print('Get Context Data')
        context = super(PatientDetailView, self).get_context_data(**kwargs)
        context['UploadFile'] = UploadFile.objects.filter(idPatient_id = self.object.pk)
        # context['UploadFile'] = UploadFile.objects.all().values()
        context['Appointment'] = Appointment.objects.filter(idPatient_id = self.object.pk)
        # context['Appointment'] = Appointment.objects.filter(idPatient_id = self.object.pk).values()
        context['Doctor'] = Doctor.objects.all().values()
        context['Budget'] = MainBudget.objects.filter(idPatient_id = self.object.pk)
        context['PaymentControl'] = PaymentControl.objects.all()
        
        #Odontogram
        context['Odontogram'] = Mouth.objects.filter(idPatient_id = self.object.pk)

        for i in context['Budget']:
            if i.State == '1':
                context['CheckBudget'] = '1'
    
        for pc in context['PaymentControl']:
            if pc.Done != True:
                for b in context['Budget']:
                    if pc.idMainBudget_id == b.id:
                        #print(pc.idMainBudget)
                        context['CheckPaymentControl'] = '1'

        for cita in context['Appointment']:
            if cita.Status == '1':
                context['CheckAppointment'] = '1'

        # Odontogram
        for odontogram in context['Odontogram']:
            if odontogram.state == '1':
                if odontogram.idPatient_id == self.object.pk:
                    context['CheckOdontogram'] = '1'

        context['form'] = self.get_form()

        return context

    def post(self, request, *args, **kwargs):
        # print('POST')
        self.object = self.get_object()
        if request.method == "POST":
            File = request.FILES["File"]
            File_file = UploadFile.objects.create(
                File=File, idPatient_id=self.object.id)
            File_path = File_file.File.path
            return HttpResponseRedirect(self.get_success_url(), {"File": File_path})
        return HttpResponseRedirect(self.get_success_url())

    def form_valid(self, form):
        # print('Form Valid')
        return super(PatientDetailView, self).form_valid(form)


def PDFView(request, id, idPatient):
    idPatient = Patient.objects.filter(id=idPatient).values()
    FileName = UploadFile.objects.filter(id=id).values()

    for document in idPatient:
        idPatient = document['id']

    for document in FileName:
        FileName = document['File']

    with open(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), f'media/{FileName}'), 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        # response['Content-Disposition'] = f'filename={Archivo}'
        return response

class FileDeleteView(DeleteView):
    model = UploadFile
    context_object_name = 'File'
    # template_name = 'dDeleteFileModal.html'
    # success_url = reverse_lazy('PatientDetailView')

    def form_valid(self, form):
        idFile = self.get_object()
        os.remove(idFile.File.path)
        return super(FileDeleteView, self).form_valid(form)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('PatientDetailView', kwargs={'pk': self.object.idPatient_id})


class RegistrarUsuarioDoctor(CreateView):
    model = Doctor
    form_class = AddDoctorForm
    template_name = 'dAddPersonal.html'
    success_url = reverse_lazy('DoctorList')

    def get_context_data(self, **kwargs):
        context = super(RegistrarUsuarioDoctor,
                        self).get_context_data(**kwargs)

        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)

        if form.is_valid():
            try:
                solicitud = form.save(commit=False)
                # print('Solicitud: ', solicitud)
                solicitud.save()

                Email = form['Email'].value()
                Username = (form['FirstName'].value() +
                            form['FirstSurname'].value())
                Password = make_password(Username.lower())
                idDoctor = (Doctor.objects.last()).id
                User = AddUser(email=Email, password=Password,
                            idDoctor_id=idDoctor)
                User.save()
                messages.success(request, 'Médico agregado')

                return HttpResponseRedirect(self.get_success_url())
            except:
                Doctor.objects.filter(id=idDoctor).delete()
                messages.error(request, 'Correo ya existente')
                return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

class DoctorList(ListView):
    model = Doctor
    template_name = "dDoctorList.html"

    def get_queryset(self):
        return self.model.objects.all()

    def get(self, request, *args, **kwargs):
        if is_ajax(request=request):
            doctorList = []
            for doctor in self.get_queryset():
                data_doctor = {}
                data_doctor['id'] = doctor.id
                data_doctor['Fullname'] = doctor.FirstName + " " + doctor.SecondName + \
                    " " + doctor.FirstSurname + " " + doctor.SecondSurname
                data_doctor['Phone'] = doctor.Phone
                data_doctor['Status'] = doctor.Status
                doctorList.append(data_doctor)
                data = json.dumps(doctorList)
            return HttpResponse(data, 'application/json')
        else:
            return render(request, self.template_name)

class DoctorUpdate(UpdateView):
    model = Doctor
    template_name = 'dAddPersonal.html'
    form_class = AddDoctorForm

    def get_context_data(self, **kwargs):
        context = super(DoctorUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)

        if 'form' not in context:
            context['form'] = self.form_class()

        context['id'] = pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_solicitud = kwargs['pk']

        solicitud = self.model.objects.get(id=id_solicitud)

        form = self.form_class(request.POST, instance=solicitud)

        if form.is_valid():
            form.save()

            mainbudget = MainBudget.objects.filter(idDoctor_id = id_solicitud)
            # print(mainbudget)
            paymentcontrol = PaymentControl.objects.all()

            # Check if there are Payments without be paid
            PaymentCheck = ''
            for i in mainbudget:
                if i.State == '0':
                    for j in paymentcontrol:
                        if i.id == j.idMainBudget_id:
                            if j.Done == False:
                                PaymentCheck = '1'

            if 'Status' in request.POST:
                obj = form.save(commit=False)
                if obj.Status == True:
                    if PaymentCheck != '1':
                        obj.Status = False
                        Appointment.objects.filter(idDoctor = id_solicitud).update(Status='0')
                        messages.info(request, 'El médico ha sido dado de baja')
                    else:
                        messages.error(request, 'No puede darse de baja, hay controles de pagos activos')
                else:
                    obj.Status = True
                    messages.success(request, 'El médico ha sido dado de alta')
                obj.save()

            return redirect('DoctorDetailView', solicitud.id)
        else:
            return redirect('DoctorDetailView', solicitud.id)


class DoctorDetailView(DetailView):
    model = Doctor
    template_name = 'dDoctorDetail.html'

    def get_success_url(self):
        return reverse('DoctorDetailView', kwargs={'pk': self.object.pk})
    
    def get_context_data(self, **kwargs):
        context = super(DoctorDetailView, self).get_context_data(**kwargs)
        context['Appointment'] = Appointment.objects.filter(idDoctor_id = self.object.pk)
        context['Patient'] = Patient.objects.all().values()
        context['Budget'] = MainBudget.objects.filter(idDoctor_id = self.object.pk)
        context['PaymentControl'] = PaymentControl.objects.all()

        for i in context['Budget']:
            if i.State == '1':
                context['CheckBudget'] = '1'
    
        for pc in context['PaymentControl']:
            if pc.Done != True:
                for b in context['Budget']:
                    if pc.idMainBudget_id == b.id:
                        context['CheckPaymentControl'] = '1'

        for cita in context['Appointment']:
            if cita.Status == '1':
                context['CheckAppointment'] = '1'

        return context


class RegistrarUsuarioAssistant(CreateView):
    model = Assistant
    form_class = AddAssistantForm
    template_name = 'dAddPersonal.html'
    success_url = reverse_lazy('AssistantList')

    def get_context_data(self, **kwargs):
        context = super(RegistrarUsuarioAssistant,
                        self).get_context_data(**kwargs)

        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)

        if form.is_valid():
            try:
                solicitud = form.save(commit=False)
                #print('Solicitud: ', solicitud)
                solicitud.save()

                Email = form['Email'].value()
                Username = (form['FirstName'].value() +
                            form['FirstSurname'].value())
                Password = make_password(Username.lower())
                idAssistant = (Assistant.objects.last()).id
                User = AddUser(email = Email, password = Password, idPersonal_id = idAssistant)
                User.save()
                messages.success(request, 'Personal agregado')

                return HttpResponseRedirect(self.get_success_url())
            except:
                Assistant.objects.filter(id=idAssistant).delete()
                messages.error(request, 'Correo ya existente')
                return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

class AssistantList(TemplateView):
    model = Assistant
    template_name = "dAssistantList.html"

    def get_queryset(self):
        return self.model.objects.all()

    def get(self, request, *args, **kwargs):
        if is_ajax(request=request):
            assistantList = []
            for assistant in self.get_queryset():
                data_assistant = {}
                data_assistant['id'] = assistant.id
                data_assistant['Fullname'] = assistant.FirstName + " " + assistant.SecondName + \
                    " " + assistant.FirstSurname + " " + assistant.SecondSurname
                data_assistant['Phone'] = assistant.Phone
                data_assistant['Status'] = assistant.Status
                assistantList.append(data_assistant)
                data = json.dumps(assistantList)
            return HttpResponse(data, 'application/json')
        else:
            return render(request, self.template_name)


class AssistantUpdate(UpdateView):
    model = Assistant
    template_name = 'dAddPersonal.html'
    form_class = AddAssistantForm

    def get_context_data(self, **kwargs):
        context = super(AssistantUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)

        if 'form' not in context:
            context['form'] = self.form_class()

        context['id'] = pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_solicitud = kwargs['pk']

        solicitud = self.model.objects.get(id=id_solicitud)

        form = self.form_class(request.POST, instance=solicitud)

        if form.is_valid():
            form.save()

            if 'Status' in request.POST:
                obj = form.save(commit=False)
                if obj.Status == True:
                    obj.Status = False
                    messages.success(request, 'El personal fue dado de baja')
                else:
                    obj.Status = True
                    messages.success(request, 'El personal fue dado de alta')
                obj.save()

            return redirect('AssistantDetailView', solicitud.id)
        else:
            return redirect('AssistantDetailView', solicitud.id)


class AssistantDetailView(DetailView):
    model = Assistant
    template_name = 'dAssistantDetail.html'


class CalendarCreateView(ListView, FormMixin):
    model = Appointment
    form_class = AddAppointmentForm
    template_name = 'dCalendar.html'
    success_url = reverse_lazy('Calendar')

    def get_context_data(self, **kwargs):
        context = super(CalendarCreateView, self).get_context_data(**kwargs)
        context['Patient'] = Patient.objects.filter(Status = '1')
        context['Doctor'] = Doctor.objects.filter(Status = '1')

        query = self.request.GET.get("InputSearch")
        context['Appointment'] = Appointment.objects.filter(idDoctor_id=query)

        if not context['Appointment']:
            context['Appointment'] = Appointment.objects.all()
        else:
            context['Appointment'] = Appointment.objects.filter(idDoctor_id = query)


        for cita in context['Appointment']:
            if cita.Status == '1':
                for patient in context['Patient']:
                    if patient.id == cita.idPatient_id:
                        for doctor in context['Doctor']:
                            if doctor.id == cita.idDoctor_id:
                                context['CheckAppointment'] = '1'

        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context


class AddAppointmentCreateView(CreateView, FormMixin):
    model = Appointment
    form_class = AddAppointmentForm
    template_name = 'dAddAppointment.html'
    success_url = reverse_lazy('Calendar')

    def get_context_data(self, **kwargs):
        context = super(AddAppointmentCreateView,
                        self).get_context_data(**kwargs)
        context['Patient'] = Patient.objects.filter(Status = '1').values()
        context['Doctor'] = Doctor.objects.filter(Status = '1').values()
        context['Appointment'] = Appointment.objects.all().values()

        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)

        if form.is_valid():
            idPatient = self.request.POST.get("InputPatient")
            idDoctor = self.request.POST.get("InputDoctor")
            Description = self.request.POST.get("Description")
            Date = self.request.POST.get("Date")

            A = Appointment(idPatient_id=idPatient, idDoctor_id=idDoctor,
                            Description=Description, Date=Date)
            A.save()
            messages.success(request, 'Cita agendada')

            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


class AppointmentUpdateView(UpdateView):
    model = Appointment
    template_name = 'dAddAppointment.html'
    form_class = AddAppointmentForm
    success_url = reverse_lazy('Calendar')

    def get_context_data(self, **kwargs):
        context = super(AppointmentUpdateView, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        context['Appointment'] = Appointment.objects.filter(id=pk)
        idPatient_id = context['Appointment'][0].idPatient_id
        idDoctor_id = context['Appointment'][0].idDoctor_id

        context['Patient'] = Patient.objects.filter(id=idPatient_id).values(
            'FirstName', 'SecondName', 'FirstSurname', 'SecondSurname')
        context['Patient'] = context['Patient'][0]

        context['Doctor'] = Doctor.objects.filter(id=idDoctor_id).values(
            'FirstName', 'SecondName', 'FirstSurname', 'SecondSurname')
        context['Doctor'] = context['Doctor'][0]

        if 'form' not in context:
            context['form'] = self.form_class()

        context['id'] = pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_solicitud = kwargs['pk']

        solicitud = self.model.objects.get(id=id_solicitud)

        form = self.form_class(request.POST, instance=solicitud)

        if form.is_valid():
            form.save()
            if 'Status' in request.POST:
                obj = form.save(commit=False)
                if obj.Status == '1':
                    obj.Status = '0'
                    messages.warning(request, 'Cita cancelada')
                # else:
                #     obj.Status = '0'
                #     messages.success(request, 'Cita actualizada')
                obj.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())


def AppointmentDoneIt(request, id):
    Change = Appointment.objects.get(id=id)
    Change.Status = '2'
    Change.save()
    messages.success(request, 'Cita realizada')

    return redirect('Calendar')


class DoctorBudgetCreateView(CreateView):
    modelP = Patient
    modelD = Doctor
    modelMB = MainBudget
    modelBF = BudgetFields
    # form_class = formset_factory(BudgetFieldForm)
    template_name = 'dAddBudget.html'    

    def get_queryset(self):
        patient = self.modelP.objects.all()
        doctor = self.modelD.objects.all()
        return patient, doctor

    def get(self, request, *args, **kwargs):
        if is_ajax(request = request):
            patients, doctors = self.get_queryset()
            
            List = []
            for patient in patients:
                data_patient = {}
                data_patient['id'] = patient.id
                data_patient['Fullname'] = patient.FirstName + " " + patient.SecondName + " " + patient.FirstSurname + " " + patient.SecondSurname
                data_patient['Role'] = "1"
                List.append(data_patient)

            for doctor in doctors:
                data_doctor = {}
                data_doctor['id'] = doctor.id
                data_doctor['Fullname'] = doctor.FirstName + " " + doctor.SecondName + " " + doctor.FirstSurname + " " + doctor.SecondSurname
                data_doctor['Role'] = "0"
                List.append(data_doctor)

            data = json.dumps(List)
            return HttpResponse(data, 'application/json')
        else:
            return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        idPatient = request.POST["idPatient"]
        idDoctor = request.POST["InputDoctor"] 

        MainBudgetDB = MainBudget(idPatient_id = idPatient, idDoctor_id = idDoctor)
        MainBudgetDB.save()
        idMainBudget = (MainBudget.objects.last()).id

        count = 0
        countII = 0
        array = []
        ids = []

        for key, value in request.POST.items():
            if key != 'csrfmiddlewaretoken':
                if key == 'idPatient' or key == 'InputDoctor':
                    ids.append(value)
                else:
                    count += 1
                    array.append(value)
                    if count == 3:
                        BudgetFieldsDB  = BudgetFields(idMainBudget_id = idMainBudget, Quantity = array[0], Treatment = array[1], Cost = array[2])
                        BudgetFieldsDB.save()
                        countII += 1
                        count = 0
                        array = []
        return redirect('BudgetFieldsDetailView', idMainBudget)

class DoctorBudgetCreateViewDoctor(CreateView):
    modelP = Patient
    modelD = Doctor
    modelMB = MainBudget
    modelBF = BudgetFields
    template_name = 'dAddBudgetDoctor.html'

    def get_queryset(self):
        patient = self.modelP.objects.all()
        doctor = self.modelD.objects.all()
        return patient, doctor

    def get(self, request, *args, **kwargs):
        if is_ajax(request = request):
            patients, doctors = self.get_queryset()
            
            List = []
            for patient in patients:
                data_patient = {}
                data_patient['id'] = patient.id
                data_patient['Fullname'] = patient.FirstName + " " + patient.SecondName + " " + patient.FirstSurname + " " + patient.SecondSurname
                data_patient['Role'] = "1"
                List.append(data_patient)

            for doctor in doctors:
                data_doctor = {}
                data_doctor['id'] = doctor.id
                data_doctor['Fullname'] = doctor.FirstName + " " + doctor.SecondName + " " + doctor.FirstSurname + " " + doctor.SecondSurname
                data_doctor['Role'] = "0"
                List.append(data_doctor)
            data = json.dumps(List)
            return HttpResponse(data, 'application/json')
        else:
            return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        idPatient = request.POST["InputPatient"]
        idDoctor = request.POST["idDoctor"]

        MainBudgetDB = MainBudget(idPatient_id = idPatient, idDoctor_id = idDoctor)
        MainBudgetDB.save()
        idMainBudget = (MainBudget.objects.last()).id

        count = 0
        countII = 0
        array = []
        ids = []

        for key, value in request.POST.items():
            if key != 'csrfmiddlewaretoken':
                if key == 'idDoctor' or key == 'InputPatient':
                    ids.append(value)
                else:
                    count += 1
                    array.append(value)
                    if count == 3:
                        BudgetFieldsDB  = BudgetFields(idMainBudget_id = idMainBudget, Quantity = array[0], Treatment = array[1], Cost = array[2])
                        BudgetFieldsDB.save()
                        countII += 1
                        count = 0
                        array = []
        return redirect('BudgetFieldsDetailView', idMainBudget)

def BudgetDeleteView(request, pk):
    Change = MainBudget.objects.get(id = pk)
    idPatient = Patient.objects.filter(id = Change.idPatient_id)
    Change.State = '2' # It means "Cancelled"
    Change.save()

    return redirect('PatientDetailView', idPatient[0].id)

class BudgetFieldsDetailView(DetailView):
    model = MainBudget
    template_name = 'dBudgetDetail.html'

    def get_success_url(self):
        return reverse('PatientDetailView', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(BudgetFieldsDetailView, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        context['BudgetFields'] = BudgetFields.objects.filter(idMainBudget_id=pk)
        context['Budget'] = MainBudget.objects.filter(id=pk)
        context['Date'] = context['Budget'][0].Date
        context['BudgetID'] = context['Budget'][0].id
        idPatient_id = context['Budget'][0].idPatient_id
        idDoctor_id = context['Budget'][0].idDoctor_id
        context['Patient'] = Patient.objects.filter(id=idPatient_id).values()
        context['Patient'] = context['Patient'][0]
        
        context['Doctor'] = Doctor.objects.filter(id=idDoctor_id).values()
        context['Doctor'] = context['Doctor'][0]

        # If the Payment Control already exists don't show the details and create budget buttons
        context['PaymentControl'] = PaymentControl.objects.filter(idMainBudget = pk)

        Total = 0
        for cost in context['BudgetFields']:
            Total = Total + (cost.Quantity * cost.Cost)

        context['Total'] = Total

        return context
    
class BudgetFieldsUpdateView(UpdateView):
    model = MainBudget
    second_model = BudgetFields
    template_name = 'dAddBudget.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(BudgetFieldsUpdateView, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        context['layout'] = 'Update'
        idMainBudget = self.model.objects.get(id=pk)
        BudgetFieldData = self.second_model.objects.filter(idMainBudget_id = idMainBudget.id)
        context['BudgetFieldData'] = BudgetFieldData
        PatientDB = Patient.objects.filter(id = idMainBudget.idPatient_id)
        context['PatientID'] = PatientDB[0].id
        context['patientName'] = PatientDB[0].FirstName + ' ' + PatientDB[0].SecondName + ' ' + PatientDB[0].FirstSurname + ' ' + PatientDB[0].SecondSurname

        doctorDB = Doctor.objects.filter(id = idMainBudget.idDoctor_id)
        context['doctorID'] = doctorDB[0].id
        context['doctorName'] = doctorDB[0].FirstName + ' ' + doctorDB[0].SecondName + ' ' + doctorDB[0].FirstSurname + ' ' + doctorDB[0].SecondSurname

        return context

    def post(self, request, *args, **kwargs):
        # idMainBudget = request.POST["idMainBudget"]
        pk = self.kwargs.get('pk', 0)
        update = BudgetFields.objects.filter(idMainBudget_id = pk)

        count = 0
        countII = 0
        array = []
        ids = []
        checkIDs = []
        checkIDsII = []

        for i in update:
            checkIDsII.append(i.id)

        for key, value in request.POST.items():
            if key != 'csrfmiddlewaretoken':
                if key == 'idMainBudget':
                    ids.append(value)
                    #print("Array: ",ids)
                else:
                    count += 1
                    array.append(value)
                    if count == 4:
                        Quantity = array[0]
                        Treatment = array[1]
                        Cost = array[2]
                        id = array[3]

                        if id == 'Empty':
                            BudgetFieldsDB  = BudgetFields(Quantity = Quantity, Treatment = Treatment, Cost = Cost, idMainBudget_id = pk)
                            BudgetFieldsDB.save()
                        else:
                            checkIDs.append(int(id))
                            change = BudgetFields.objects.get(id = id)

                            if str(update[countII].Quantity) != Quantity:
                                change.Quantity = Quantity
                                change.save()
                                
                            if str(update[countII].Treatment) != Treatment:
                                change.Treatment = Treatment
                                change.save()

                            if str(update[countII].Cost) != Cost:
                                change.Cost = Cost
                                change.save()
                        
                        countII += 1
                        count = 0
                        array = []
        
        deleted = set(checkIDsII).difference(checkIDs)
        messages.success(request, 'Presupuesto actualizado')

        for i in range(len(deleted)):
            if list(deleted)[i] != None:
                # print(list(deleted)[i])
                BudgetFields.objects.filter(id=list(deleted)[i]).delete()
        return redirect('BudgetFieldsDetailView', pk)


def CreatePayment(request, id):
    BudgetID = MainBudget.objects.filter(id = id)

    idBudget = BudgetID[0].id

    # PatientID = BudgetID[0].idPatient_id

    Cost = BudgetFields.objects.filter(idMainBudget_id = idBudget)

    Total = 0
    for cost in Cost:
        Total = Total + (cost.Quantity * cost.Cost)

    Payment = PaymentControl(idMainBudget_id = idBudget, Credit = Total)
    Payment.save()

    ChangeState = MainBudget.objects.get(id = idBudget)
    ChangeState.State = '0'
    ChangeState.save()
    messages.success(request, 'Control de pagos creado')

    return redirect('DoctorPaymentBalance', idBudget)


class DoctorPaymentList(TemplateView):
    model = PaymentControl
    template_name = "dPaymentsList.html"

    def get_queryset(self):
        return self.model.objects.all()

    def get(self, request, *args, **kwargs): 
        if is_ajax(request=request):
            mainBudget = MainBudget.objects.all()
            patient = Patient.objects.all()
            paymentList = []
            for payment in self.get_queryset():
                for budget in mainBudget:
                    if budget.id == payment.idMainBudget_id:
                        if payment.Done == False:
                            for patients in patient:
                                if budget.idPatient_id == patients.id:
                                    data_payment = {}
                                    data_payment['id'] = payment.id
                                    data_payment['BudgetFK'] = payment.idMainBudget_id
                                    data_payment['BudgetID'] = budget.id
                                    data_payment['paymentDone'] = payment.Done
                                    data_payment['PatientFullName'] = patients.FirstName + ' ' + patients.SecondName + ' ' + patients.FirstSurname + ' ' + patients.SecondSurname
                                    data_payment['PatientID'] = patients.id
                                    paymentList.append(data_payment)
                                    data = json.dumps(paymentList)
            return HttpResponse(data, 'application/json')
        else:
            return render(request, self.template_name)
        
class DoctorPaymentBalance(UpdateView):
    model = MainBudget
    template_name = 'dPaymentUpdate.html'
    fields = '__all__'
    success_url = reverse_lazy('DoctorPaymentList')

    def get_context_data(self, **kwargs):
        context = super(DoctorPaymentBalance, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        # print('El PK es: ', pk)
        InitialPayment = PaymentControl.objects.filter(idMainBudget_id = pk)[0].Credit
        context['PaymentDone'] = PaymentControl.objects.filter(idMainBudget_id = pk)[0].Done
        # print(context['PaymentDone'])

        context['Budget'] = MainBudget.objects.filter(id = pk)
        idPatient_id = context['Budget'][0].idPatient_id
        idDoctor_id = context['Budget'][0].idDoctor_id

        context['BudgetFields'] = BudgetFields.objects.filter(idMainBudget_id = pk)
        context['Date'] = context['Budget'][0].Date

        context['Patient'] = Patient.objects.filter(id=idPatient_id).values(
            'FirstName', 'SecondName', 'FirstSurname', 'SecondSurname')
        context['Patient'] = context['Patient'][0]

        context['Doctor'] = Doctor.objects.filter(id=idDoctor_id).values(
            'FirstName', 'SecondName', 'FirstSurname', 'SecondSurname')
        context['Doctor'] = context['Doctor'][0]

        Debt = PaymentDone.objects.filter(idMainBudget_id = pk)

        if not Debt:
            context['PaymentControl'] = PaymentControl.objects.filter(idMainBudget_id = pk)[0].Credit
        else:
            Total = 0
            for i in Debt:
                Total = Total + i.Paid

            context['PaymentControl'] = InitialPayment - Total
            
            context['Pays'] = PaymentDone.objects.filter(idMainBudget_id = pk)

        context['id'] = pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        pk = kwargs['pk']
        Paid = request.POST['InputPayment']

        Pay = PaymentDone(Paid = Paid, idMainBudget_id = pk)
        Pay.save()

        Amounts = PaymentDone.objects.filter(idMainBudget_id = pk)
        Control = PaymentControl.objects.filter(idMainBudget_id = pk)

        Total = 0
        for i in Amounts:
            Total = Total + i.Paid

        if Total == Control[0].Credit:
            Dones = PaymentControl.objects.get(idMainBudget_id = pk)
            Dones.Done = True
            messages.success(request, 'Ha terminado de pagar el tratamiento')
            Dones.save()
        else:
            messages.success(request, 'Ha realizado un abono')

        # return HttpResponseRedirect(self.get_success_url())
        return redirect('DoctorPaymentBalance', pk)
    
class PaymentDoneHistory(ListView):
    model = MainBudget
    template_name = "dHistory.html"

    def get_context_data(self, **kwargs):
        context = super(PaymentDoneHistory, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        context['Span'] = 'HP'
        context['What'] = '0'
        context['PK'] = pk
        context['MainBudget'] = MainBudget.objects.all()
        context['Patient'] = Patient.objects.filter(id = pk)[0].id
        context['Data'] = PaymentControl.objects.all()
        context['Doctor'] = Doctor.objects.all()

        for j in context['MainBudget']:
            for i in context['Data']:
                if j.id == i.idMainBudget_id:
                    if j.idPatient_id == context['Patient']:
                        if i.Done == True:
                            context['CheckPaymentDoneHistory'] = '1'

        return context
    
class AppointmentsHistory(ListView):
    model = Appointment
    template_name = "dHistory.html"

    def get_context_data(self, **kwargs):
        context = super(AppointmentsHistory, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        context['Span'] = 'HC'
        context['What'] = '0'
        context['PK'] = pk
        context['Appointments'] = Appointment.objects.all()
        context['Patient'] = Patient.objects.filter(id = pk)[0].id

        for i in context['Appointments']:
            if i.Status != '1':
                if i.idPatient_id == context['Patient']:
                    context['CheckAppointmentsHistory'] = '1'

        return context
    
class BudgetsHistory(ListView):
    model = MainBudget
    template_name = "dHistory.html"

    def get_context_data(self, **kwargs):
        context = super(BudgetsHistory, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        context['Span'] = 'HB'
        context['What'] = '0'
        context['PK'] = pk
        context['Budget'] = MainBudget.objects.all()
        context['Patient'] = Patient.objects.filter(id = pk)[0].id

        for i in context['Budget']:
            if i.State == '0':
                if i.idPatient_id == context['Patient']:
                    context['CheckBudgetsHistory'] = '1'

        return context
    
class PaymentDoneHistoryD(ListView):
    model = MainBudget
    template_name = "dHistory.html"

    def get_context_data(self, **kwargs):
        context = super(PaymentDoneHistoryD, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        context['Span'] = 'HP'
        context['What'] = '1'
        context['PK'] = pk
        context['MainBudget'] = MainBudget.objects.all()
        context['Doctor'] = Doctor.objects.filter(id = pk)[0].id
        context['Data'] = PaymentControl.objects.all()
        for j in context['MainBudget']:
            for i in context['Data']:
                if j.id == i.idMainBudget_id:
                    if j.idDoctor_id == context['Doctor']:
                        if i.Done == True:
                            #print(i.id)
                            context['CheckPaymentDoneHistory'] = '1'

        return context
    
class AppointmentsHistoryD(ListView):
    model = Appointment
    template_name = "dHistory.html"

    def get_context_data(self, **kwargs):
        context = super(AppointmentsHistoryD, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        context['Span'] = 'HC'
        context['What'] = '1'
        context['PK'] = pk
        context['Appointments'] = Appointment.objects.all()
        context['Doctor'] = Doctor.objects.filter(id = pk)[0].id

        for i in context['Appointments']:
            if i.Status != '1':
                if i.idDoctor_id == context['Doctor']:
                    context['CheckAppointmentsHistory'] = '1'

        return context
    
# Odontogram

# Create an Odontogram
def NewOdonto(request, pk):
    # patient = Patient.objects.filter(id = pk)
    odontogram = Mouth.objects.create(idPatient_id=pk)
    # append odontogram to profile
    if request.method == 'POST':
        return redirect('Tooth', pk_mouth=odontogram.id)
    # return render(request, 'dOdontogram.html', {
    #     'odontogram': odontogram,
    #     }
    # )
    return redirect('OdontogramView', pk_mouth=odontogram.id)

# Show the Odontogram in General
def OdontoView(request, pk_mouth):
    odontogram = Mouth.objects.get(pk = pk_mouth)
    treatments = [
        'sano', 'c1', 'c2', 'c3', 'c4', 'c5',
        'r1', 'r2', 'r3', 'r4', 'r5',
        'e', 'N', 'PL', 'p', 'z', 'd', 'g',
    ]
    if request.method == 'POST':
        return redirect('Tooth', pk_mouth = pk_mouth)
    return render(request, 'dOdontogram.html', {
        'odontogram': odontogram,
        'pk_mouth': pk_mouth,
        'treatments': treatments,
        }
    )

# Delete Odontogram
def DeleteOdontogram(request, pk):
    odontogram = Mouth.objects.get(id = pk)
    idPatient = odontogram.idPatient_id
    odontogram.state = '0'
    odontogram.save()
    return redirect('PatientDetailView', idPatient)

# Odontogram History
class OdontogramHistory(ListView):
    model = Mouth
    template_name = "dHistory.html"

    def get_context_data(self, **kwargs):
        context = super(OdontogramHistory, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        context['Span'] = 'HO'
        context['What'] = '0'
        context['PK'] = pk
        context['Mouth'] = Mouth.objects.all()
        context['Patient'] = Patient.objects.filter(id = pk)[0].id

        for i in context['Mouth']:
            if i.state == '0':
                if i.idPatient_id == context['Patient']:
                    context['CheckOdontogramHistory'] = '1'

        return context

# Show the Tooth in Detail and Save
def Tooth(request, pk_mouth, nb_tooth):
    # nb_tooth
    # form = forms.T11Form(request.POST)
    odontogram = Mouth.objects.get(pk=pk_mouth)
    # Selection of field
    if nb_tooth == 't_11':
        #print(odontogram.t_11)
        tooth_form = forms.T11Form(instance=odontogram)
    elif nb_tooth == 't_12':
        tooth_form = forms.T12Form(instance=odontogram)
    elif nb_tooth == 't_13':
        tooth_form = forms.T13Form(instance=odontogram)
    elif nb_tooth == 't_14':
        tooth_form = forms.T14Form(instance=odontogram)
    elif nb_tooth == 't_15':
        tooth_form = forms.T15Form(instance=odontogram)
    elif nb_tooth == 't_16':
        tooth_form = forms.T16Form(instance=odontogram)
    elif nb_tooth == 't_17':
        tooth_form = forms.T17Form(instance=odontogram)
    elif nb_tooth == 't_18':
        tooth_form = forms.T18Form(instance=odontogram)
    elif nb_tooth == 't_21':
        tooth_form = forms.T21Form(instance=odontogram)
    elif nb_tooth == 't_22':
        tooth_form = forms.T22Form(instance=odontogram)
    elif nb_tooth == 't_23':
        tooth_form = forms.T23Form(instance=odontogram)
    elif nb_tooth == 't_24':
        tooth_form = forms.T24Form(instance=odontogram)
    elif nb_tooth == 't_25':
        tooth_form = forms.T25Form(instance=odontogram)
    elif nb_tooth == 't_26':
        tooth_form = forms.T26Form(instance=odontogram)
    elif nb_tooth == 't_27':
        tooth_form = forms.T27Form(instance=odontogram)
    elif nb_tooth == 't_28':
        tooth_form = forms.T28Form(instance=odontogram)
    elif nb_tooth == 't_31':
        tooth_form = forms.T31Form(instance=odontogram)
    elif nb_tooth == 't_32':
        tooth_form = forms.T32Form(instance=odontogram)
    elif nb_tooth == 't_33':
        tooth_form = forms.T33Form(instance=odontogram)
    elif nb_tooth == 't_34':
        tooth_form = forms.T34Form(instance=odontogram)
    elif nb_tooth == 't_35':
        tooth_form = forms.T35Form(instance=odontogram)
    elif nb_tooth == 't_36':
        tooth_form = forms.T36Form(instance=odontogram)
    elif nb_tooth == 't_37':
        tooth_form = forms.T37Form(instance=odontogram)
    elif nb_tooth == 't_38':
        tooth_form = forms.T38Form(instance=odontogram)
    elif nb_tooth == 't_41':
        tooth_form = forms.T41Form(instance=odontogram)
    elif nb_tooth == 't_42':
        tooth_form = forms.T42Form(instance=odontogram)
    elif nb_tooth == 't_43':
        tooth_form = forms.T43Form(instance=odontogram)
    elif nb_tooth == 't_44':
        tooth_form = forms.T44Form(instance=odontogram)
    elif nb_tooth == 't_45':
        tooth_form = forms.T45Form(instance=odontogram)
    elif nb_tooth == 't_46':
        tooth_form = forms.T46Form(instance=odontogram)
    elif nb_tooth == 't_47':
        tooth_form = forms.T47Form(instance=odontogram)
    elif nb_tooth == 't_48':
        tooth_form = forms.T48Form(instance=odontogram)
    elif nb_tooth == 't_51':
        tooth_form = forms.T51Form(instance=odontogram)
    elif nb_tooth == 't_52':
        tooth_form = forms.T52Form(instance=odontogram)
    elif nb_tooth == 't_53':
        tooth_form = forms.T53Form(instance=odontogram)
    elif nb_tooth == 't_54':
        tooth_form = forms.T54Form(instance=odontogram)
    elif nb_tooth == 't_55':
        tooth_form = forms.T55Form(instance=odontogram)
    elif nb_tooth == 't_61':
        tooth_form = forms.T61Form(instance=odontogram)
    elif nb_tooth == 't_62':
        tooth_form = forms.T62Form(instance=odontogram)
    elif nb_tooth == 't_63':
        tooth_form = forms.T63Form(instance=odontogram)
    elif nb_tooth == 't_64':
        tooth_form = forms.T64Form(instance=odontogram)
    elif nb_tooth == 't_65':
        tooth_form = forms.T65Form(instance=odontogram)
    elif nb_tooth == 't_71':
        tooth_form = forms.T71Form(instance=odontogram)
    elif nb_tooth == 't_72':
        tooth_form = forms.T72Form(instance=odontogram)
    elif nb_tooth == 't_73':
        tooth_form = forms.T73Form(instance=odontogram)
    elif nb_tooth == 't_74':
        tooth_form = forms.T74Form(instance=odontogram)
    elif nb_tooth == 't_75':
        tooth_form = forms.T75Form(instance=odontogram)
    elif nb_tooth == 't_81':
        tooth_form = forms.T81Form(instance=odontogram)
    elif nb_tooth == 't_82':
        tooth_form = forms.T82Form(instance=odontogram)
    elif nb_tooth == 't_83':
        tooth_form = forms.T83Form(instance=odontogram)
    elif nb_tooth == 't_84':
        tooth_form = forms.T84Form(instance=odontogram)
    else:
        tooth_form = forms.T85Form(instance=odontogram)
    if request.method == 'POST':
        # Selection of field
        if nb_tooth == 't_11':
            tooth_form = forms.T11Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_12':
            tooth_form = forms.T12Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_13':
            tooth_form = forms.T13Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_14':
            tooth_form = forms.T14Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_15':
            tooth_form = forms.T15Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_16':
            tooth_form = forms.T16Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_17':
            tooth_form = forms.T17Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_18':
            tooth_form = forms.T18Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_21':
            tooth_form = forms.T21Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_22':
            tooth_form = forms.T22Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_23':
            tooth_form = forms.T23Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_24':
            tooth_form = forms.T24Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_25':
            tooth_form = forms.T25Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_26':
            tooth_form = forms.T26Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_27':
            tooth_form = forms.T27Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_28':
            tooth_form = forms.T28Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_31':
            tooth_form = forms.T31Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_32':
            tooth_form = forms.T32Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_33':
            tooth_form = forms.T33Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_34':
            tooth_form = forms.T34Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_35':
            tooth_form = forms.T35Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_36':
            tooth_form = forms.T36Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_37':
            tooth_form = forms.T37Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_38':
            tooth_form = forms.T38Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_41':
            tooth_form = forms.T41Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_42':
            tooth_form = forms.T42Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_43':
            tooth_form = forms.T43Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_44':
            tooth_form = forms.T44Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_45':
            tooth_form = forms.T45Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_46':
            tooth_form = forms.T46Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_47':
            tooth_form = forms.T47Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_48':
            tooth_form = forms.T48Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_51':
            tooth_form = forms.T51Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_52':
            tooth_form = forms.T52Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_53':
            tooth_form = forms.T53Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_54':
            tooth_form = forms.T54Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_55':
            tooth_form = forms.T55Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_61':
            tooth_form = forms.T61Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_62':
            tooth_form = forms.T62Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_63':
            tooth_form = forms.T63Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_64':
            tooth_form = forms.T64Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_65':
            tooth_form = forms.T65Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_71':
            tooth_form = forms.T71Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_72':
            tooth_form = forms.T72Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_73':
            tooth_form = forms.T73Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_74':
            tooth_form = forms.T74Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_75':
            tooth_form = forms.T75Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_81':
            tooth_form = forms.T81Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_82':
            tooth_form = forms.T82Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_83':
            tooth_form = forms.T83Form(
                request.POST, instance=odontogram)
        elif nb_tooth == 't_84':
            tooth_form = forms.T84Form(
                request.POST, instance=odontogram)
        else:
            tooth_form = forms.T85Form(
                request.POST, instance=odontogram)
        if tooth_form.is_valid():
            # append to profile            
            tooth_form.save()
            return redirect('OdontogramView', pk_mouth = pk_mouth)
    return render(request, 'dTooth.html', {
        'tooth_form': tooth_form,
        'pk_mouth': pk_mouth,
        'nb_tooth': nb_tooth,
        }
    )
# BackUp
# import glob
# from django.core.management import call_command
# class BackUpView(TemplateView):
#     template_name = 'dBackUp.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         fileName = []
#         fileNameMedia = []
#         for file_name in glob.iglob('/Users/wesleyjiang/Desktop/Development/Django/Clínica Dental Integral Especializada/CDIE/backups/*.dump', recursive=True):
#             words = file_name.partition('backups')[2]
#             fileName.append(words)
#             # print(words[-1])

#         for file_name in glob.iglob('/Users/wesleyjiang/Desktop/Development/Django/Clínica Dental Integral Especializada/CDIE/backups/*.tar', recursive=True):
#             words = file_name.partition('backups')[2]
#             fileNameMedia.append(words)
#             # print(words[-1])

#         context['File'] = fileName
#         context['FileMedia'] = fileNameMedia
#         return context
    

#     def post(self, request, *args, **kwargs):
#         try:
#             if request.method == 'POST':
#                 if 'Backup' in request.POST:
#                     call_command('dbbackup')
#                     call_command('mediabackup')
#                 # if 'Restore' in request.POST:
#                 #     file = request.POST.get('RestoreInput')
#                 #     call_command('dbrestore --noinput -i ' + file)
#         except:
#             pass
#         return redirect('BackUp')