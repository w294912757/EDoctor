from backend.methods import *


def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    return login_method(username, password)


def add_user(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    usertype = request.POST.get('usertype', '')
    operatorId = request.POST.get('operatorId', '')
    qualifications = request.FILES.getlist('qualifications')
    photos = request.FILES.getlist('photos')
    return add_user_method(username, password, usertype, operatorId, qualifications, photos, request.POST)


def delete_user(request):
    id = request.POST.get('id', '')
    operatorId = request.POST.get('operatorId', '')
    return delete_user_method(id, operatorId)


def show_user(request):
    return show_user_method(request)


def query_user(request):
    keyword = request.POST.get('keyword', '')
    searchtype = request.POST.get('searchtype', '')
    operatorId = request.POST.get('operatorId', '')
    return query_user_method(keyword, searchtype, operatorId)


def alter_user(request):
    id = request.POST.get('id', '')
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    operatorId = request.POST.get('operatorId', '')
    return alter_user_method(id, username, password, operatorId)


def add_clinic(request):
    name = request.POST.get('name', '')
    department = request.POST.get('department', '')
    address = request.POST.get('address', '')
    phoneNum = request.POST.get('phoneNum', '')
    userId = request.POST.get('userId', '')
    operatorId = request.POST.get('operatorId', '')
    return add_clinic_method(name, department, address, phoneNum, userId, operatorId)


def delete_clinic(request):
    id = request.POST.get('id', '')
    operatorId = request.POST.get('operatorId', '')
    return delete_clinic_method(id, operatorId)


def show_clinic(request):
    status = request.POST.get('status', '')
    return show_clinic_method(status)


def query_clinic(request):
    keyword = request.POST.get('keyword', '')
    searchtype = request.POST.get('searchtype', '')
    operatorId = request.POST.get('operatorId', '')
    return query_clinic_method(keyword, searchtype, operatorId)


def alter_clinic(request):
    id = request.POST.get('id', '')
    name = request.POST.get('name', '')
    department = request.POST.get('department', '')
    address = request.POST.get('address', '')
    phoneNum = request.POST.get('phoneNum', '')
    userId = request.POST.get('userId', '')
    operatorId = request.POST.get('operatorId', '')
    return alter_clinic_method(id, name, department, address, phoneNum, userId, operatorId)


def add_doctor(request):
    name = request.POST.get('name', '')
    department = request.POST.get('department', '')
    sex = request.POST.get('sex', '')
    age = request.POST.get('age', '')
    userId = request.POST.get('userId', '')
    clinicId = request.POST.get('clinicId', '')
    operatorId = request.POST.get('operatorId', '')
    return add_doctor_method(name, department, sex, age, userId, clinicId, operatorId)


def delete_doctor(request):
    id = request.POST.get('id', '')
    operatorId = request.POST.get('operatorId', '')
    return delete_doctor_method(id, operatorId)


def show_doctor(request):
    status = request.POST.get('status', '')
    return show_doctor_method(status)


def query_doctor(request):
    keyword = request.POST.get('keyword', '')
    searchtype = request.POST.get('searchtype', '')
    operatorId = request.POST.get('operatorId', '')
    return query_doctor_method(keyword, searchtype, operatorId)


def alter_doctor(request):
    id = request.POST.get('id', '')
    name = request.POST.get('name', '')
    department = request.POST.get('department', '')
    sex = request.POST.get('sex', '')
    age = request.POST.get('age', '')
    userId = request.POST.get('userId', '')
    clinicId = request.POST.get('clinicId', '')
    operatorId = request.POST.get('operatorId', '')
    return alter_doctor_method(id, name, department, sex, age, userId, clinicId, operatorId)


def add_prescription(request):
    patientName = request.POST.get('patientName', '')
    sex = request.POST.get('sex', '')
    age = request.POST.get('age', '')
    phoneNum = request.POST.get('phoneNum', '')
    diagnosis = request.POST.get('diagnosis', '')
    feature = request.POST.get('feature', '')
    treatment = request.POST.get('treatment', '')
    doctorId = request.POST.get('doctorId', '')
    operatorId = request.POST.get('operatorId', '')
    return add_prescription_method(patientName, sex, age, phoneNum, diagnosis, feature, treatment, doctorId, operatorId,
                                   )


def delete_prescription(request):
    id = request.POST.get('id', '')
    operatorId = request.POST.get('operatorId', '')
    return delete_prescription_method(id, operatorId)


def show_prescription(request):
    return show_prescription_method()


def query_prescription(request):
    keyword = request.POST.get('keyword', '')
    searchtype = request.POST.get('searchtype', '')
    operatorId = request.POST.get('operatorId', '')
    return query_prescription_method(keyword, searchtype, operatorId)


def alter_prescription(request):
    id = request.POST.get('id', '')
    patientName = request.POST.get('patientName', '')
    sex = request.POST.get('sex', '')
    age = request.POST.get('age', '')
    phoneNum = request.POST.get('phoneNum', '')
    diagnosis = request.POST.get('diagnosis', '')
    feature = request.POST.get('feature', '')
    treatment = request.POST.get('treatment', '')
    doctorId = request.POST.get('doctorId', '')
    operatorId = request.POST.get('operatorId', '')
    return alter_prescription_method(id, patientName, sex, age, phoneNum, diagnosis, feature, treatment, doctorId,
                                     operatorId)


def get_image(request):
    id = request.POST.get('id', '')
    ownerType = request.POST.get('ownerType', '')
    imageType = request.POST.get('imageType', '')
    operatorId = request.POST.get('operatorId', '')
    return get_image_method(id, ownerType, imageType, operatorId)


def change_user_authority(request):
    id = request.POST.get('id', '')
    usertype = request.POST.get('usertype', '')
    operatorId = request.POST.get('operatorId', '')
    changeTo = request.POST.get('changeTo', '')
    return change_user_authority_method(id, usertype, operatorId, changeTo)


def date_type_statistic(request):
    date1 = request.POST.get('date1', '')
    date2 = request.POST.get('date2', '')
    operatortype = request.POST.get('operatortype', '')
    statistictype = request.POST.get('statistictype', '')
    userid = request.POST.get('userid', '')
    doctorid = request.POST.get('doctorid', '')
    date1strings = date1.split('-')
    date2strings = date2.split('-')
    date1arr = list(map(int, date1strings))
    date2arr = list(map(int, date2strings))
    date = np.array([date1arr, date2arr])
    return date_type_statistic_method(date, userid,doctorid, operatortype, statistictype)
