from Apps.Doctor.models import Patient, Doctor, Assistant


def add_variable_to_context(request):
    try:
        if request.user.is_authenticated and request.user.usuario_administrador:
            return {
                'testme': 'Bienvenido, Administrador'
            }
        elif request.user.is_authenticated and request.user.idPatient_id == request.user.idPatient_id:
            user = request.user
            idUser = user.idPatient_id
            sex = Patient.objects.values_list('Sex').get(pk=idUser)
            mydata = Patient.objects.values_list(
                'FirstName', 'FirstSurname').get(pk=idUser)
            sex = ''.join(sex)
            mydata = ' '.join(mydata)

            if sex == '0':
                Message = 'Bienvenida, ' + mydata
            else:
                Message = 'Bienvenido, ' + mydata

            return {
                'testme': Message
            }
        elif request.user.is_authenticated and request.user.idDoctor_id == request.user.idDoctor_id:

            user = request.user
            idUser = user.idDoctor_id
            sex = Doctor.objects.values_list('Sex').get(pk=idUser)
            mydata = Doctor.objects.values_list(
                'FirstName', 'FirstSurname').get(pk=idUser)
            sex = ''.join(sex)
            mydata = ' '.join(mydata)

            if sex == '0':
                Message = 'Bienvenida, ' + mydata
            else:
                Message = 'Bienvenido, ' + mydata

            return {
                'testme': Message
            }
        elif request.user.is_authenticated and request.user.idPersonal_id == request.user.idPersonal_id:

            user = request.user
            idUser = user.idPersonal_id
            sex = Assistant.objects.values_list('Sex').get(pk=idUser)
            mydata = Assistant.objects.values_list(
                'FirstName', 'FirstSurname').get(pk=idUser)
            sex = ''.join(sex)
            mydata = ' '.join(mydata)

            if sex == '0':
                Message = 'Bienvenida, ' + mydata
            else:
                Message = 'Bienvenido, ' + mydata

            return {
                'testme': Message
            }
    except Patient.DoesNotExist:
        # do something here
    
        return {}
