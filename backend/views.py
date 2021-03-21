import os

from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse

from EDoctor import settings
from backend.models import *
from django.db.models import Q
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
    image = request.FILES.get('image')
    return add_user_method(username, password, usertype, operatorId, image)


def delete_user(request):
    id = request.POST.get('id', '')
    operatorId = request.POST.get('operatorId', '')
    return delete_user_method(id, operatorId)


def show_user(request):
    return show_user_method()


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
    return show_clinic_method()


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
    doctor = Doctor.objects.get(id=id)
    doctor.delete()
    DoctorLog.objects.create(dataId=id, operationType='delete id:', originData=id, resultData='',
                             operatorId=operatorId)
    return JsonResponse({'message': '医生删除成功'})


def show_doctor(request):
    doctors = Doctor.objects.all()
    data = []
    for i in doctors:
        doctor = {}
        # 给字典添加键值对
        doctor['id'] = i.id
        doctor['name'] = i.name
        doctor['department'] = i.department
        doctor['sex'] = i.sex
        doctor['age'] = i.age
        doctor['userId'] = i.userId.id
        doctor['clinicId'] = i.clinicId.id
        doctor['clinicName'] = i.clinicId.name
        data.append(doctor)
    return JsonResponse({'message': '查询成功', 'data': data})


def query_doctor(request):
    keyword = request.POST.get('keyword', '')
    searchtype = request.POST.get('searchtype', '')
    operatorId = request.POST.get('operatorId', '')
    data = {}
    if searchtype == 'id':
        try:
            result = Doctor.objects.get(id=keyword)
        except ObjectDoesNotExist:
            return JsonResponse({'message': '查询对象结果为空'})

        else:
            # 给字典添加键值对
            data['id'] = result.id
            data['name'] = result.name
            data['department'] = result.department
            data['sex'] = result.sex
            data['age'] = result.age
            data['userId'] = result.userId.id
            data['clinicId'] = result.clinicId.id
            data['clinicName'] = result.clinicId.name
        DoctorLog.objects.create(dataId=result.id, operationType='query by id:', originData=keyword,
                                 resultData='',
                                 operatorId=operatorId)
        return JsonResponse({'message': '查询成功', 'data': data})

    if searchtype == 'name':
        result = Doctor.objects.filter(name__contains=keyword)
        if result:
            data = []
            for i in result:
                doctor = {}
                # 给字典添加键值对
                doctor['id'] = i.id
                doctor['name'] = i.name
                doctor['department'] = i.department
                doctor['sex'] = i.sex
                doctor['age'] = i.age
                doctor['userId'] = i.userId.id
                doctor['clinicId'] = i.clinicId.id
                doctor['clinicName'] = i.clinicId.name
                data.append(doctor)
            DoctorLog.objects.create(dataId=data[0].id, operationType='query by name:', originData=keyword,
                                     resultData='',
                                     operatorId=operatorId)
            return JsonResponse({'message': '查询成功', 'data': data})
        else:
            return JsonResponse({'message': '查询的数据不存在'})
    if searchtype == 'sex':
        result = Doctor.objects.filter(sex__contains=keyword)
        if result:
            data = []
            for i in result:
                doctor = {}
                # 给字典添加键值对
                doctor['id'] = i.id
                doctor['name'] = i.name
                doctor['department'] = i.department
                doctor['sex'] = i.sex
                doctor['age'] = i.age
                doctor['userId'] = i.userId.id
                doctor['clinicId'] = i.clinicId.id
                doctor['clinicName'] = i.clinicId.name
                data.append(doctor)
            DoctorLog.objects.create(dataId=data[0].id, operationType='query by sex:', originData=keyword,
                                     resultData='',
                                     operatorId=operatorId)
            return JsonResponse({'message': '查询成功', 'data': data})
        else:
            return JsonResponse({'message': '查询的数据不存在'})
    if searchtype == 'age':
        result = Doctor.objects.filter(age__contains=keyword)
        if result:
            data = []
            for i in result:
                doctor = {}
                # 给字典添加键值对
                doctor['id'] = i.id
                doctor['name'] = i.name
                doctor['department'] = i.department
                doctor['sex'] = i.sex
                doctor['age'] = i.age
                doctor['userId'] = i.userId.id
                doctor['clinicId'] = i.clinicId.id
                doctor['clinicName'] = i.clinicId.name
                data.append(doctor)
            DoctorLog.objects.create(dataId=data[0].id, operationType='query by age:', originData=keyword,
                                     resultData='',
                                     operatorId=operatorId)
            return JsonResponse({'message': '查询成功', 'data': data})
        else:
            return JsonResponse({'message': '查询的数据不存在'})
    if searchtype == 'userId':
        result = Doctor.objects.filter(userId__contains=keyword)
        if result:
            data = []
            for i in result:
                doctor = {}
                # 给字典添加键值对
                doctor['id'] = i.id
                doctor['name'] = i.name
                doctor['department'] = i.department
                doctor['sex'] = i.sex
                doctor['age'] = i.age
                doctor['userId'] = i.userId.id
                doctor['clinicId'] = i.clinicId.id
                doctor['clinicName'] = i.clinicId.name
                data.append(doctor)
            DoctorLog.objects.create(dataId=data[0].id, operationType='query by userId:', originData=keyword,
                                     resultData='',
                                     operatorId=operatorId)
            return JsonResponse({'message': '查询成功', 'data': data})
        else:
            return JsonResponse({'message': '查询的数据不存在'})
    if searchtype == 'clinicId':
        result = Doctor.objects.filter(clinicId__contains=keyword)
        if result:
            data = []
            for i in result:
                doctor = {}
                # 给字典添加键值对
                doctor['id'] = i.id
                doctor['name'] = i.name
                doctor['department'] = i.department
                doctor['sex'] = i.sex
                doctor['age'] = i.age
                doctor['userId'] = i.userId.id
                doctor['clinicId'] = i.clinicId.id
                doctor['clinicName'] = i.clinicId.name
                data.append(doctor)
            DoctorLog.objects.create(dataId=data[0].id, operationType='query by clinicId:', originData=keyword,
                                     resultData='',
                                     operatorId=operatorId)
            return JsonResponse({'message': '查询成功', 'data': data})
        else:
            return JsonResponse({'message': '查询的数据不存在'})
    if searchtype == 'all':
        result = Doctor.objects.filter(
            Q(name__contains=keyword) | Q(department__contains=keyword) | Q(sex__contains=keyword) | Q(
                age__contains=keyword) | Q(
                userId__contains=keyword) | Q(
                clinicId__contains=keyword))
        if result:
            data = []
            for i in result:
                doctor = {}
                doctor['id'] = i.id
                doctor['name'] = i.name
                doctor['department'] = i.department
                doctor['sex'] = i.sex
                doctor['age'] = i.age
                doctor['userId'] = i.userId.id
                doctor['clinicId'] = i.clinicId.id
                doctor['clinicName'] = i.clinicId.name
                data.append(doctor)
            DoctorLog.objects.create(dataId=data[0].id, operationType='mumble query:', originData=keyword,
                                     resultData='',
                                     operatorId=operatorId)
            return JsonResponse({'message': '查询成功', 'data': data})
        else:
            return JsonResponse({'message': '查询的数据不存在'})


def alter_doctor(request):
    id = request.POST.get('id', '')
    name = request.POST.get('name', '')
    department = request.POST.get('department', '')
    sex = request.POST.get('sex', '')
    age = request.POST.get('age', '')
    userId = request.POST.get('userId', '')
    clinicId = request.POST.get('clinicId', '')
    operatorId = request.POST.get('operatorId', '')
    originDoctor = Doctor.objects.get(id=id)
    if name != '':
        Doctor.objects.filter(id=id).update(name=name)
        DoctorLog.objects.create(dataId=id, operationType='alter name:', originData=originDoctor.name,
                                 resultData=name,
                                 operatorId=operatorId)
    if department != '':
        Doctor.objects.filter(id=id).update(department=department)
        DoctorLog.objects.create(dataId=id, operationType='alter department:', originData=originDoctor.department,
                                 resultData=sex,
                                 operatorId=operatorId)
    if sex != '':
        Doctor.objects.filter(id=id).update(sex=sex)
        DoctorLog.objects.create(dataId=id, operationType='alter sex:', originData=originDoctor.sex,
                                 resultData=sex,
                                 operatorId=operatorId)
    if age != '':
        Doctor.objects.filter(id=id).update(age=age)
        DoctorLog.objects.create(dataId=id, operationType='alter age:', originData=originDoctor.age,
                                 resultData=age,
                                 operatorId=operatorId)
    if userId != '':
        Doctor.objects.filter(id=id).update(userId=userId)
        DoctorLog.objects.create(dataId=id, operationType='alter userId:', originData=originDoctor.userId,
                                 resultData=userId,
                                 operatorId=operatorId)
    if clinicId != '':
        Doctor.objects.filter(id=id).update(clinicId=clinicId)
        DoctorLog.objects.create(dataId=id, operationType='alter clinicId:', originData=originDoctor.clinicId,
                                 resultData=clinicId,
                                 operatorId=operatorId)
    return JsonResponse({'message': '医生更改成功'})


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
    doctor = Doctor.objects.get(id=doctorId)
    Prescription.objects.create(patientName=patientName, sex=sex, age=age, phoneNum=phoneNum, diagnosis=diagnosis,
                                feature=feature, treatment=treatment, doctorId=doctor)
    latestPrescriptionId = Prescription.objects.latest('id').id
    resultData = 'patientName:' + patientName + ' sex:' + sex + ' age:' + age + ' phoneNum:' + phoneNum + ' diagnosis:' + diagnosis + ' feature:' + feature + ' treatment:' + treatment + ' doctorId:' + doctorId
    PrescriptionLog.objects.create(dataId=latestPrescriptionId, operationType='add', originData='',
                                   resultData=resultData,
                                   operatorId=operatorId)
    return JsonResponse({'message': '病历添加成功'})


def delete_prescription(request):
    id = request.POST.get('id', '')
    operatorId = request.POST.get('operatorId', '')
    prescription = Prescription.objects.get(id=id)
    prescription.delete()
    PrescriptionLog.objects.create(dataId=id, operationType='delete by id', originData=id,
                                   resultData='',
                                   operatorId=operatorId)
    return JsonResponse({'message': '病历删除成功'})


def show_prescription(request):
    prescriptions = Prescription.objects.all()
    data = []
    for i in prescriptions:
        prescription = {}
        # 给字典添加键值对
        prescription['id'] = i.id
        prescription['patientName'] = i.patientName
        prescription['sex'] = i.sex
        prescription['age'] = i.age
        prescription['phoneNum'] = i.phoneNum
        prescription['diagnosis'] = i.diagnosis
        prescription['feature'] = i.feature
        prescription['treatment'] = i.treatment
        prescription['doctorId'] = i.doctorId.id
        data.append(prescription)
    return JsonResponse({'message': '查询成功', 'data': data})


def query_prescription(request):
    keyword = request.POST.get('keyword', '')
    searchtype = request.POST.get('searchtype', '')
    operatorId = request.POST.get('operatorId', '')
    data = {}
    if searchtype == 'id':
        try:
            result = Prescription.objects.get(id=keyword)
        except ObjectDoesNotExist:
            return JsonResponse({'message': '查询对象结果为空'})

        else:
            # 给字典添加键值对
            data['id'] = result.id
            data['patientName'] = result.patientName
            data['sex'] = result.sex
            data['age'] = result.age
            data['phoneNum'] = result.phoneNum
            data['diagnosis'] = result.diagnosis
            data['feature'] = result.feature
            data['treatment'] = result.treatment
            data['doctorId'] = result.doctorId.id
        PrescriptionLog.objects.create(dataId=result.id, operationType='query by id', originData=keyword,
                                       resultData='',
                                       operatorId=operatorId)
        return JsonResponse({'message': '查询成功', 'data': data})

    if searchtype == 'patientName':
        result = Prescription.objects.filter(patientName__contains=keyword)
        if result:
            data = []
            for i in result:
                prescription = {}
                # 给字典添加键值对
                prescription['id'] = i.id
                prescription['patientName'] = i.patientName
                prescription['sex'] = i.sex
                prescription['age'] = i.age
                prescription['phoneNum'] = i.phoneNum
                prescription['diagnosis'] = i.diagnosis
                prescription['feature'] = i.feature
                prescription['treatment'] = i.treatment
                prescription['doctorId'] = i.doctorId.id
                data.append(prescription)
            PrescriptionLog.objects.create(dataId=data[0].id, operationType='query by patientName', originData=keyword,
                                           resultData='',
                                           operatorId=operatorId)
            return JsonResponse({'message': '查询成功', 'data': data})
        else:
            return JsonResponse({'message': '查询的数据不存在'})
    if searchtype == 'sex':
        result = Prescription.objects.filter(sex__contains=keyword)
        if result:
            data = []
            for i in result:
                prescription = {}
                # 给字典添加键值对
                prescription['id'] = i.id
                prescription['patientName'] = i.patientName
                prescription['sex'] = i.sex
                prescription['age'] = i.age
                prescription['phoneNum'] = i.phoneNum
                prescription['diagnosis'] = i.diagnosis
                prescription['feature'] = i.feature
                prescription['treatment'] = i.treatment
                prescription['doctorId'] = i.doctorId.id
                data.append(prescription)
            PrescriptionLog.objects.create(dataId=data[0].id, operationType='query by sex', originData=keyword,
                                           resultData='',
                                           operatorId=operatorId)
            return JsonResponse({'message': '查询成功', 'data': data})
        else:
            return JsonResponse({'message': '查询的数据不存在'})
    if searchtype == 'age':
        result = Prescription.objects.filter(age__contains=keyword)
        if result:
            data = []
            for i in result:
                prescription = {}
                # 给字典添加键值对
                prescription['id'] = i.id
                prescription['patientName'] = i.patientName
                prescription['sex'] = i.sex
                prescription['age'] = i.age
                prescription['phoneNum'] = i.phoneNum
                prescription['diagnosis'] = i.diagnosis
                prescription['feature'] = i.feature
                prescription['treatment'] = i.treatment
                prescription['doctorId'] = i.doctorId.id
                data.append(prescription)
            PrescriptionLog.objects.create(dataId=data[0].id, operationType='query by age', originData=keyword,
                                           resultData='',
                                           operatorId=operatorId)
            return JsonResponse({'message': '查询成功', 'data': data})
        else:
            return JsonResponse({'message': '查询的数据不存在'})
    if searchtype == 'phoneNum':
        result = Prescription.objects.filter(phoneNum__contains=keyword)
        if result:
            data = []
            for i in result:
                prescription = {}
                # 给字典添加键值对
                prescription['id'] = i.id
                prescription['patientName'] = i.patientName
                prescription['sex'] = i.sex
                prescription['age'] = i.age
                prescription['phoneNum'] = i.phoneNum
                prescription['diagnosis'] = i.diagnosis
                prescription['feature'] = i.feature
                prescription['treatment'] = i.treatment
                prescription['doctorId'] = i.doctorId.id
                data.append(prescription)
            PrescriptionLog.objects.create(dataId=data[0].id, operationType='query by phoneNum', originData=keyword,
                                           resultData='',
                                           operatorId=operatorId)
            return JsonResponse({'message': '查询成功', 'data': data})
        else:
            return JsonResponse({'message': '查询的数据不存在'})
    if searchtype == 'diagnosis':
        result = Prescription.objects.filter(diagnosis__contains=keyword)
        if result:
            data = []
            for i in result:
                prescription = {}
                # 给字典添加键值对
                prescription['id'] = i.id
                prescription['patientName'] = i.patientName
                prescription['sex'] = i.sex
                prescription['age'] = i.age
                prescription['phoneNum'] = i.phoneNum
                prescription['diagnosis'] = i.diagnosis
                prescription['feature'] = i.feature
                prescription['treatment'] = i.treatment
                prescription['doctorId'] = i.doctorId.id
                data.append(prescription)
            PrescriptionLog.objects.create(dataId=data[0].id, operationType='query by diagnosis', originData=keyword,
                                           resultData='',
                                           operatorId=operatorId)
            return JsonResponse({'message': '查询成功', 'data': data})
        else:
            return JsonResponse({'message': '查询的数据不存在'})
    if searchtype == 'feature':
        result = Prescription.objects.filter(feature__contains=keyword)
        if result:
            data = []
            for i in result:
                prescription = {}
                # 给字典添加键值对
                prescription['id'] = i.id
                prescription['patientName'] = i.patientName
                prescription['sex'] = i.sex
                prescription['age'] = i.age
                prescription['phoneNum'] = i.phoneNum
                prescription['diagnosis'] = i.diagnosis
                prescription['feature'] = i.feature
                prescription['treatment'] = i.treatment
                prescription['doctorId'] = i.doctorId.id
                data.append(prescription)
            PrescriptionLog.objects.create(dataId=data[0].id, operationType='query by feature', originData=keyword,
                                           resultData='',
                                           operatorId=operatorId)
            return JsonResponse({'message': '查询成功', 'data': data})
        else:
            return JsonResponse({'message': '查询的数据不存在'})
    if searchtype == 'treatment':
        result = Prescription.objects.filter(treatment__contains=keyword)
        if result:
            data = []
            for i in result:
                prescription = {}
                # 给字典添加键值对
                prescription['id'] = i.id
                prescription['patientName'] = i.patientName
                prescription['sex'] = i.sex
                prescription['age'] = i.age
                prescription['phoneNum'] = i.phoneNum
                prescription['diagnosis'] = i.diagnosis
                prescription['feature'] = i.feature
                prescription['treatment'] = i.treatment
                prescription['doctorId'] = i.doctorId.id
                data.append(prescription)
            PrescriptionLog.objects.create(dataId=data[0].id, operationType='query by treatment', originData=keyword,
                                           resultData='',
                                           operatorId=operatorId)
            return JsonResponse({'message': '查询成功', 'data': data})
        else:
            return JsonResponse({'message': '查询的数据不存在'})
    if searchtype == 'doctorId':
        result = Prescription.objects.filter(doctorId__contains=keyword)
        if result:
            data = []
            for i in result:
                prescription = {}
                # 给字典添加键值对
                prescription['id'] = i.id
                prescription['patientName'] = i.patientName
                prescription['sex'] = i.sex
                prescription['age'] = i.age
                prescription['phoneNum'] = i.phoneNum
                prescription['diagnosis'] = i.diagnosis
                prescription['feature'] = i.feature
                prescription['treatment'] = i.treatment
                prescription['doctorId'] = i.doctorId.id
                data.append(prescription)
            PrescriptionLog.objects.create(dataId=data[0].id, operationType='query by doctorId', originData=keyword,
                                           resultData='',
                                           operatorId=operatorId)
            return JsonResponse({'message': '查询成功', 'data': data})
        else:
            return JsonResponse({'message': '查询的数据不存在'})
    if searchtype == 'all':
        result = Doctor.objects.filter(
            Q(patientName__contains=keyword) | Q(sex__contains=keyword) | Q(age__contains=keyword) | Q(
                phoneNum__contains=keyword) | Q(
                diagnosis__contains=keyword) | Q(feature__contains=keyword) | Q(treatment__contains=keyword) | Q(
                doctorId__contains=keyword))
        if result:
            data = []
            for i in result:
                prescription = {}
                # 给字典添加键值对
                prescription['id'] = i.id
                prescription['patientName'] = i.patientName
                prescription['sex'] = i.sex
                prescription['age'] = i.age
                prescription['phoneNum'] = i.phoneNum
                prescription['diagnosis'] = i.diagnosis
                prescription['feature'] = i.feature
                prescription['treatment'] = i.treatment
                prescription['doctorId'] = i.doctorId.id
                data.append(prescription)
            PrescriptionLog.objects.create(dataId=data[0].id, operationType='mumble query', originData=keyword,
                                           resultData='',
                                           operatorId=operatorId)
            return JsonResponse({'message': '查询成功', 'data': data})
        else:
            return JsonResponse({'message': '查询的数据不存在'})


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
    originPrescription = Prescription.objects.get(id=id)
    if patientName != '':
        Prescription.objects.filter(id=id).update(patientName=patientName)
        PrescriptionLog.objects.create(dataId=id, operationType='alter patientName',
                                       originData=originPrescription.patientName,
                                       resultData=patientName,
                                       operatorId=operatorId)
    if sex != '':
        Prescription.objects.filter(id=id).update(sex=sex)
        PrescriptionLog.objects.create(dataId=id, operationType='alter sex',
                                       originData=originPrescription.sex,
                                       resultData=sex,
                                       operatorId=operatorId)
    if age != '':
        Prescription.objects.filter(id=id).update(age=age)
        PrescriptionLog.objects.create(dataId=id, operationType='alter age',
                                       originData=originPrescription.age,
                                       resultData=age,
                                       operatorId=operatorId)
    if phoneNum != '':
        Prescription.objects.filter(id=id).update(phoneNum=phoneNum)
        PrescriptionLog.objects.create(dataId=id, operationType='alter phoneNum',
                                       originData=originPrescription.phoneNum,
                                       resultData=phoneNum,
                                       operatorId=operatorId)
    if diagnosis != '':
        Prescription.objects.filter(id=id).update(diagnosis=diagnosis)
        PrescriptionLog.objects.create(dataId=id, operationType='alter diagnosis',
                                       originData=originPrescription.diagnosis,
                                       resultData=diagnosis,
                                       operatorId=operatorId)
    if feature != '':
        Prescription.objects.filter(id=id).update(feature=feature)
        PrescriptionLog.objects.create(dataId=id, operationType='alter feature',
                                       originData=originPrescription.feature,
                                       resultData=feature,
                                       operatorId=operatorId)
    if treatment != '':
        Prescription.objects.filter(id=id).update(treatment=treatment)
        PrescriptionLog.objects.create(dataId=id, operationType='alter treatment',
                                       originData=originPrescription.treatment,
                                       resultData=treatment,
                                       operatorId=operatorId)
    if doctorId != '':
        Prescription.objects.filter(id=id).update(doctorId=doctorId)
        PrescriptionLog.objects.create(dataId=id, operationType='alter doctorId',
                                       originData=originPrescription.doctorId,
                                       resultData=doctorId,
                                       operatorId=operatorId)
    return JsonResponse({'message': '病历更改成功'})
