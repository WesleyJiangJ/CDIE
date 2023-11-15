from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.decorators import login_required
from Apps.Doctor.views import DoctorIndex, RegistrarUsuario, PatientList, PatientUpdate, PatientDetailView, FileDeleteView, PDFView, DoctorList, RegistrarUsuarioDoctor, RegistrarUsuarioAssistant, AssistantList, DoctorUpdate, DoctorDetailView, AssistantDetailView, AssistantUpdate, CalendarCreateView, AppointmentUpdateView, AddAppointmentCreateView, AppointmentDoneIt, DoctorBudgetCreateView, BudgetFieldsDetailView, BudgetFieldsUpdateView, CreatePayment, DoctorPaymentList, DoctorPaymentBalance, PaymentDoneHistory, AppointmentsHistory, BudgetsHistory, PaymentDoneHistoryD, AppointmentsHistoryD, DoctorBudgetCreateViewDoctor, BudgetDeleteView, Tooth, OdontoView, NewOdonto, DeleteOdontogram, OdontogramHistory

urlpatterns = [
    path('', login_required(DoctorIndex.as_view()), name='DoctorIndex'),
    path('patient/', login_required(PatientList.as_view()), name='DoctorPatient'),
    path('addpatient/', login_required(RegistrarUsuario.as_view()), name='DoctorAddPatient'),
    path('editar/<pk>', login_required(PatientUpdate.as_view()), name="PatientUpdate"),
    path('detail/<pk>', login_required(PatientDetailView.as_view()), name='PatientDetailView'),

    path('file/<int:id>/<int:idPatient>', login_required(PDFView), name='DisplayPdfView'),
    path('delete/<pk>', login_required(FileDeleteView.as_view()), name='FileDeleteView'),

    path('doctorlist/', login_required(DoctorList.as_view()), name='DoctorList'),
    path('adddoctor/', login_required(RegistrarUsuarioDoctor.as_view()), name='RegistrarUsuarioDoctor'),
    path('detaildoctor/<pk>', login_required(DoctorDetailView.as_view()), name='DoctorDetailView'),
    path('editdoctor/<pk>', login_required(DoctorUpdate.as_view()), name="DoctorUpdate"),

    path('assistantlist/', login_required(AssistantList.as_view()), name='AssistantList'),
    path('detailassistant/<pk>', login_required(AssistantDetailView.as_view()), name='AssistantDetailView'),
    path('editassistant/<pk>', login_required(AssistantUpdate.as_view()), name="AssistantUpdate"),
    path('addassistant/', login_required(RegistrarUsuarioAssistant.as_view()), name='RegistrarUsuarioAssistant'),

    path('calendar/', login_required(CalendarCreateView.as_view()), name='Calendar'),
    path('addappointment/', login_required(AddAppointmentCreateView.as_view()), name='AddAppointmentCreateView'),
    path('editappointment/<pk>', login_required(AppointmentUpdateView.as_view()), name='AppointmentUpdateView'),
    path('appointmentcheckit/<int:id>', login_required(AppointmentDoneIt), name='AppointmentDoneIt'),

    path('budget/<pk>', login_required(DoctorBudgetCreateView.as_view()), name='DoctorBudget'),
    path('budgetdoctor/<pk>', login_required(DoctorBudgetCreateViewDoctor.as_view()), name='DoctorBudgetDoctor'),
    path('budgetdetail/<pk>', login_required(BudgetFieldsDetailView.as_view()), name='BudgetFieldsDetailView'),
    path('budgetupdate/<pk>', login_required(BudgetFieldsUpdateView.as_view()), name='BudgetFieldsUpdateView'),
    path('budgetdelete/<pk>', login_required(BudgetDeleteView), name='BudgetDeleteView'),

    path('payments/', login_required(DoctorPaymentList.as_view()), name='DoctorPaymentList'),
    path('createpayment/<int:id>', login_required(CreatePayment), name='CreatePayment'),
    path('paymentbalance/<pk>', login_required(DoctorPaymentBalance.as_view()), name='DoctorPaymentBalance'),
    
    path('paymentshistory/<pk>', login_required(PaymentDoneHistory.as_view()), name='PaymentDoneHistory'),
    path('appointmentshistory/<pk>', login_required(AppointmentsHistory.as_view()), name='AppointmentHistory'),
    path('budgetshistory/<pk>', login_required(BudgetsHistory.as_view()), name='BudgetHistory'),

    path('paymentshistoryd/<pk>', login_required(PaymentDoneHistoryD.as_view()), name='PaymentDoneHistoryD'),
    path('appointmentshistoryd/<pk>', login_required(AppointmentsHistoryD.as_view()), name='AppointmentsHistoryD'),

    # Odontogram
    # Show the Tooth in Detail and Save
    path('tooth/<pk_mouth>/<nb_tooth>/', login_required(Tooth), name='Tooth'),
    # Show the Odontogram in General
    path('odontogram/<pk_mouth>', login_required(OdontoView), name='OdontogramView'),
    # Create an Odontogram
    path('newodontogram/<pk>', login_required(NewOdonto), name='NewOdontogram'),
    # Delete an Odontogram
    path('deleteodontogram/<pk>', login_required(DeleteOdontogram), name='DeleteOdontogram'),
    # Odontogram Hostory
    path('odontogramhistory/<pk>', login_required(OdontogramHistory.as_view()), name='OdontogramHistory'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
