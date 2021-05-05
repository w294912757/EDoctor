import json
import os
from datetime import datetime

from django.utils import timezone
import pytz
import numpy as np
from django.core import serializers
from django.http import JsonResponse

from EDoctor import settings
from backend.models import *
from django.db.models import Q


def login_method(username, password):
    resultSet = User.objects.filter(username=username)
    if not resultSet:
        # 用户不存在
        return JsonResponse({'checkCode': '1'})
    else:
        result = resultSet[0]
        if password == result.password:
            # 未被授权
            if (result.authorized == False):
                return JsonResponse({'checkCode': '4'})
            # 登陆成功
            operatorId = result.id
            usertype = result.usertype
            # 称呼
            title = ''
            userId = ''
            if usertype == '1':
                title = Clinic.objects.get(userId=operatorId).name
                userId = Clinic.objects.get(userId=operatorId).id
            elif usertype == '2':
                title = Doctor.objects.get(userId=operatorId).name
                userId = Doctor.objects.get(userId=operatorId).id
            elif usertype == '3':
                title = User.objects.get(id=operatorId).username
            UserLog.objects.create(dataId=operatorId, operationType='login', originData='', resultData='',
                                   operatorId=operatorId)
            response = JsonResponse({'checkCode': '2', 'title': title})
            response.set_cookie('operatorId', operatorId)
            response.set_cookie('usertype', usertype)
            if usertype == '1':
                response.set_cookie('clinicId', userId)
            elif usertype == '2':
                response.set_cookie('doctorId', userId)
            return response
        else:
            # 密码错误
            return JsonResponse({'checkCode': '3'})


def add_user_method(username, password, usertype, operatorId, qualifications, photos, data):
    result = User.objects.filter(username=username)
    if not result:
        User.objects.create(username=username, password=password, usertype=usertype)
        latestUserId = User.objects.latest('id').id
        latestId = ''
        qualificationPath = ''
        photoPath = ''
        if (usertype == '1'):
            add_clinic_method(data.get('name', ''), data.get('department', ''), data.get('address', ''),
                              data.get('phoneNum', ''), latestUserId, latestUserId)
            latestId = Clinic.objects.latest('id').id
            qualificationPath = os.path.join(settings.UPLOAD_FILE, 'clinics', str(latestId), 'qualification')
            photoPath = os.path.join(settings.UPLOAD_FILE, 'clinics', str(latestId), 'photo')

        else:
            clinicIdOfDoctor = data.get('clinicIdOfDoctor', '')
            add_doctor_method(data.get('name', ''), data.get('department', ''),
                              data.get('sex', ''), data.get('age', ''), latestUserId,
                              clinicIdOfDoctor, operatorId)
            latestId = Doctor.objects.latest('id').id
            qualificationPath = os.path.join(settings.UPLOAD_FILE, 'doctors', str(latestId), 'qualification')
            photoPath = os.path.join(settings.UPLOAD_FILE, 'doctors', str(latestId), 'photo')

        os.makedirs(qualificationPath)
        for qualification in qualifications:
            imageFilename = os.path.join(qualificationPath, qualification.name)
            f = open(imageFilename, 'wb')
            for i in qualification.chunks():
                f.write(i)
            f.close()

        os.makedirs(photoPath)
        for photo in photos:
            imageFilename = os.path.join(photoPath, photo.name)
            f = open(imageFilename, 'wb')
            for i in photo.chunks():
                f.write(i)
            f.close()

        resultData = 'username:' + username + ' password:' + password + ' usertype:' + usertype
        operationType = 'add'
        if operatorId == '':
            operationType = 'signUp'
        UserLog.objects.create(dataId=latestUserId, operationType=operationType, originData='',
                               resultData=resultData,
                               operatorId=operatorId)

        return JsonResponse({'message': '用户添加成功，等待管理员批准'})

    else:
        return JsonResponse({'checkCode': '3'})


def delete_user_method(id, operatorId):
    user = User.objects.filter(id=id)
    user.delete()
    UserLog.objects.create(dataId=id, operationType='delete id:', originData=id, resultData='',
                           operatorId=operatorId)
    return JsonResponse({'message': '用户删除成功'})


def show_user_method(data):
    users = User.objects.all()
    data = []
    for i in users:
        user = {}
        # 给字典添加键值对
        user['id'] = i.id
        user['username'] = i.username
        user['password'] = i.password
        if i.usertype == '1':
            user['object'] = json.loads(serializers.serialize("json", Clinic.objects.filter(userId=i.id)))
        elif i.usertype == '2':
            user['object'] = json.loads(serializers.serialize("json", Doctor.objects.filter(userId=i.id)))
        data.append(user)
    return JsonResponse({'message': '查询成功', 'data': data})


def query_user_method(keyword, searchtype, operatorId):
    data = {}
    if searchtype == 'id':
        result = User.objects.filter(id=keyword)
        if not result:
            return JsonResponse({'message': '查询对象结果为空'})

        else:
            # 给字典添加键值对
            result = result[0]
            data['id'] = result.id
            data['username'] = result.username
            data['password'] = result.password
            data['usertype'] = result.usertype
        UserLog.objects.create(dataId=keyword, operationType='query by id', originData=keyword, resultData='',
                               operatorId=operatorId)
        return JsonResponse({'message': '查询成功', 'data': data})

    if searchtype == 'username':
        result = User.objects.filter(username=keyword)
        if not result:
            return JsonResponse({'message': '查询对象结果为空'})

        else:
            # 给字典添加键值对
            result = result[0]
            data['id'] = result.id
            data['username'] = result.username
            data['password'] = result.password
            data['usertype'] = result.usertype
        UserLog.objects.create(dataId=result.id, operationType='query by username', originData=keyword, resultData='',
                               operatorId=operatorId)
        return JsonResponse({'message': '查询成功', 'data': data})


def alter_user_method(id, username, password, operatorId):
    originUser = User.objects.filter(id=id)
    if username != '':
        User.objects.filter(id=id).update(username=username)
        UserLog.objects.create(dataId=id, operationType='alter username', originData=originUser.username,
                               resultData=username,
                               operatorId=operatorId)
    if password != '':
        User.objects.filter(id=id).update(password=password)
        UserLog.objects.create(dataId=id, operationType='alter password', originData=originUser.password,
                               resultData=password,
                               operatorId=operatorId)
    return JsonResponse({'message': '用户更改成功'})


def add_clinic_method(name, department, address, phoneNum, userId, operatorId):
    user = User.objects.filter(id=userId)
    Clinic.objects.create(name=name, address=address, phoneNum=phoneNum, userId=user[0], department=department)
    latestClinicId = Clinic.objects.latest('id').id
    resultData = 'name:' + name + ' department:' + department + ' address:' + address + ' phoneNum:' + phoneNum
    ClinicLog.objects.create(dataId=latestClinicId, operationType='add', originData='', resultData=resultData,
                             operatorId=operatorId)
    return JsonResponse({'message': '诊所添加成功'})


def delete_clinic_method(id, operatorId):
    clinic = Clinic.objects.filter(id=id)
    clinic.delete()
    ClinicLog.objects.create(dataId=id, operationType='delete id:', originData=id, resultData='',
                             operatorId=operatorId)
    return JsonResponse({'message': '诊所删除成功'})


def show_clinic_method(status):
    clinics = Clinic.objects.all()
    data = []
    if status == '2':
        # 默认返回所有诊所
        for i in clinics:
            clinic = {}
            # 给字典添加键值对
            clinic['id'] = i.id
            clinic['name'] = i.name
            clinic['department'] = i.department
            clinic['address'] = i.address
            clinic['phoneNum'] = i.phoneNum
            clinic['userId'] = i.userId.id
            data.append(clinic)
    elif status == '0':
        # 等待授权的诊所
        for i in clinics:
            if i.userId.authorized == 1:
                continue
            clinic = {}
            # 给字典添加键值对
            clinic['id'] = i.id
            clinic['name'] = i.name
            clinic['department'] = i.department
            clinic['address'] = i.address
            clinic['phoneNum'] = i.phoneNum
            clinic['userId'] = i.userId.id
            data.append(clinic)
    elif status == '1':
        # 已授权的诊所
        for i in clinics:
            if i.userId.authorized == 0:
                continue
            clinic = {}
            # 给字典添加键值对
            clinic['id'] = i.id
            clinic['name'] = i.name
            clinic['department'] = i.department
            clinic['address'] = i.address
            clinic['phoneNum'] = i.phoneNum
            clinic['userId'] = i.userId.id
            data.append(clinic)
    return JsonResponse({'message': '查询成功', 'data': data})


def query_clinic_method(keyword, searchtype, operatorId):
    data = {}
    if searchtype == 'id':
        result = Clinic.objects.filter(id=keyword)
        if not result:
            return JsonResponse({'message': '查询对象结果为空'})

        else:
            # 给字典添加键值对
            result = result[0]
            data['id'] = result.id
            data['name'] = result.name
            data['department'] = result.department
            data['address'] = result.address
            data['phoneNum'] = result.phoneNum
            data['userId'] = result.userId.id
        ClinicLog.objects.create(dataId=keyword, operationType='query by id:', originData=keyword, resultData='',
                                 operatorId=operatorId)
        return JsonResponse({'message': '查询成功', 'data': data})

    if searchtype == 'name':
        result = Clinic.objects.filter(name__contains=keyword)
        if result:
            data = []
            for i in result:
                clinic = {}
                # 给字典添加键值对
                clinic['id'] = i.id
                clinic['name'] = i.name
                clinic['department'] = i.department
                clinic['address'] = i.address
                clinic['phoneNum'] = i.phoneNum
                clinic['userId'] = i.userId.id
                data.append(clinic)
            ClinicLog.objects.create(dataId=data[0].id, operationType='query by name:', originData=keyword,
                                     resultData='',
                                     operatorId=operatorId)
            return JsonResponse({'message': '查询成功', 'data': data})
        else:
            return JsonResponse({'message': '查询的数据不存在'})
    if searchtype == 'department':
        result = Clinic.objects.filter(name__contains=keyword)
        if result:
            data = []
            for i in result:
                clinic = {}
                # 给字典添加键值对
                clinic['id'] = i.id
                clinic['department'] = i.department
                clinic['name'] = i.name
                clinic['address'] = i.address
                clinic['phoneNum'] = i.phoneNum
                clinic['userId'] = i.userId.id
                data.append(clinic)
            ClinicLog.objects.create(dataId=data[0].id, operationType='query by name:', originData=keyword,
                                     resultData='',
                                     operatorId=operatorId)
            return JsonResponse({'message': '查询成功', 'data': data})
        else:
            return JsonResponse({'message': '查询的数据不存在'})
    if searchtype == 'address':
        result = Clinic.objects.filter(address__contains=keyword)
        if result:
            data = []
            for i in result:
                clinic = {}
                # 给字典添加键值对
                clinic['id'] = i.id
                clinic['name'] = i.name
                clinic['department'] = i.department
                clinic['address'] = i.address
                clinic['phoneNum'] = i.phoneNum
                clinic['userId'] = i.userId.id
                data.append(clinic)
            ClinicLog.objects.create(dataId=data[0].id, operationType='query by address:', originData=keyword,
                                     resultData='',
                                     operatorId=operatorId)
            return JsonResponse({'message': '查询成功', 'data': data})
        else:
            return JsonResponse({'message': '查询的数据不存在'})
    if searchtype == 'phoneNum':
        result = Clinic.objects.filter(phoneNum__contains=keyword)
        if result:
            data = []
            for i in result:
                clinic = {}
                # 给字典添加键值对
                clinic['id'] = i.id
                clinic['name'] = i.name
                clinic['department'] = i.department
                clinic['address'] = i.address
                clinic['phoneNum'] = i.phoneNum
                clinic['userId'] = i.userId.id
                data.append(clinic)
            ClinicLog.objects.create(dataId=data[0].id, operationType='query by phoneNum:', originData=keyword,
                                     resultData='',
                                     operatorId=operatorId)
            return JsonResponse({'message': '查询成功', 'data': data})
        else:
            return JsonResponse({'message': '查询的数据不存在'})
    if searchtype == 'userId':
        result = Clinic.objects.filter(userId__contains=keyword)
        if result:
            data = []
            for i in result:
                clinic = {}
                # 给字典添加键值对
                clinic['id'] = i.id
                clinic['name'] = i.name
                clinic['department'] = i.department
                clinic['address'] = i.address
                clinic['phoneNum'] = i.phoneNum
                clinic['userId'] = i.userId.id
                data.append(clinic)
            ClinicLog.objects.create(dataId=data[0].id, operationType='query by userId:', originData=keyword,
                                     resultData='',
                                     operatorId=operatorId)
            return JsonResponse({'message': '查询成功', 'data': data})
        else:
            return JsonResponse({'message': '查询的数据不存在'})
    if searchtype == 'all':
        result = Clinic.objects.filter(
            Q(name__contains=keyword) | Q(department__contains=keyword) | Q(address__contains=keyword) | Q(
                phoneNum__contains=keyword))
        if result:
            data = []
            for i in result:
                clinic = {}
                # 给字典添加键值对
                clinic['id'] = i.id
                clinic['name'] = i.name
                clinic['department'] = i.department
                clinic['address'] = i.address
                clinic['phoneNum'] = i.phoneNum
                clinic['userId'] = i.userId.id
                data.append(clinic)
            ClinicLog.objects.create(dataId=data[0].id, operationType='mumble query:', originData=keyword,
                                     resultData='',
                                     operatorId=operatorId)
            return JsonResponse({'message': '查询成功', 'data': data})
        else:
            return JsonResponse({'message': '查询的数据不存在'})


def alter_clinic_method(id, name, department, address, phoneNum, userId, operatorId):
    originClinic = Clinic.objects.filter(id=id)
    if name != '':
        Clinic.objects.filter(id=id).update(name=name)
        ClinicLog.objects.create(dataId=id, operationType='alter name', originData=originClinic.name,
                                 resultData=name,
                                 operatorId=operatorId)
    if department != '':
        Clinic.objects.filter(id=id).update(department=department)
        ClinicLog.objects.create(dataId=id, operationType='alter department', originData=originClinic.department,
                                 resultData=department,
                                 operatorId=operatorId)
    if address != '':
        Clinic.objects.filter(id=id).update(address=address)
        ClinicLog.objects.create(dataId=id, operationType='alter address', originData=originClinic.address,
                                 resultData=address,
                                 operatorId=operatorId)
    if phoneNum != '':
        Clinic.objects.filter(id=id).update(phoneNum=phoneNum)
        ClinicLog.objects.create(dataId=id, operationType='alter address', originData=originClinic.phoneNum,
                                 resultData=phoneNum,
                                 operatorId=operatorId)
    if userId != '':
        Clinic.objects.filter(id=id).update(userId=userId)
        ClinicLog.objects.create(dataId=id, operationType='alter userId:', originData=originClinic.userId,
                                 resultData=userId,
                                 operatorId=operatorId)
    return JsonResponse({'message': '诊所更改成功'})


def add_doctor_method(name, department, sex, age, userId, clinicId, operatorId):
    user = User.objects.get(id=userId)
    clinic = Clinic.objects.get(id=clinicId)
    Doctor.objects.create(name=name, department=department, sex=sex, age=age, userId=user, clinicId=clinic)
    latestDoctorId = Doctor.objects.latest('id').id
    resultData = 'name:' + name + 'department:' + department + ' sex:' + sex + ' age:' + age + ' userId:' + str(
        userId) + ' clinicId:' + str(clinicId)
    DoctorLog.objects.create(dataId=latestDoctorId, operationType='add', originData='', resultData=resultData,
                             operatorId=operatorId)
    return JsonResponse({'message': '医生添加成功'})


def delete_doctor_method(id, operatorId):
    doctor = Doctor.objects.filter(id=id)
    doctor.delete()
    DoctorLog.objects.create(dataId=id, operationType='delete id:', originData=id, resultData='',
                             operatorId=operatorId)
    return JsonResponse({'message': '医生删除成功'})


def show_doctor_method(status):
    doctors = Doctor.objects.all()
    data = []
    if status == '2':
        # 默认返回所有诊所
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
    elif status == '0':
        # 等待授权的诊所
        for i in doctors:
            if i.userId.authorized == 1:
                continue
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
    elif status == '1':
        # 已授权的诊所
        for i in doctors:
            if i.userId.authorized == 0:
                continue
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


def query_doctor_method(keyword, searchtype, operatorId):
    data = {}
    if searchtype == 'id':
        result = Doctor.objects.filter(id=keyword)
        if not result:
            return JsonResponse({'message': '查询对象结果为空'})

        else:
            # 给字典添加键值对
            result = result[0]
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
        result = Doctor.objects.filter(clinicId=keyword)
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
            DoctorLog.objects.create(dataId='', operationType='query by clinicId:', originData=keyword,
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


def alter_doctor_method(id, name, department, sex, age, userId, clinicId, operatorId):
    originDoctor = Doctor.objects.filter(id=id)
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


def add_prescription_method(patientName, sex, age, phoneNum, diagnosis, feature, treatment, doctorId, operatorId,
                            ):
    doctor = Doctor.objects.get(id=doctorId)
    Prescription.objects.create(patientName=patientName, sex=sex, age=age, phoneNum=phoneNum, diagnosis=diagnosis,
                                feature=feature, treatment=treatment, doctorId=doctor)
    latestPrescriptionId = Prescription.objects.latest('id').id
    photoPath = os.path.join(settings.UPLOAD_FILE, 'prescriptions', str(latestPrescriptionId))
    os.makedirs(photoPath)

    resultData = 'patientName:' + patientName + ' sex:' + sex + ' age:' + age + ' phoneNum:' + phoneNum + ' diagnosis:' + diagnosis + ' feature:' + feature + ' treatment:' + treatment + ' doctorId:' + doctorId
    PrescriptionLog.objects.create(dataId=latestPrescriptionId, operationType='add', originData='',
                                   resultData=resultData,
                                   operatorId=operatorId)
    return JsonResponse({'message': '病历添加成功'})


def delete_prescription_method(id, operatorId):
    prescription = Prescription.objects.filter(id=id)
    prescription.delete()
    PrescriptionLog.objects.create(dataId=id, operationType='delete by id', originData=id,
                                   resultData='',
                                   operatorId=operatorId)
    return JsonResponse({'message': '病历删除成功'})


def show_prescription_method():
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


def query_prescription_method(keyword, searchtype, operatorId):
    data = {}
    if searchtype == 'id':
        result = Prescription.objects.get(id=keyword)
        if not result:
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
        result = Prescription.objects.filter(doctorId=keyword)
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
            PrescriptionLog.objects.create(dataId='', operationType='query by doctorId', originData=keyword,
                                           resultData='',
                                           operatorId=operatorId)
            return JsonResponse({'message': '查询成功', 'data': data})
        else:
            return JsonResponse({'message': '查询的数据不存在'})
    if searchtype == 'clinicId':
        doctors = Doctor.objects.filter(clinicId=keyword)
        result = []
        for doctor in doctors:
            result.append(Prescription.objects.get(doctorId=doctor.id))
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
                prescription['doctorName'] = i.doctorId.name
                data.append(prescription)
            PrescriptionLog.objects.create(dataId='', operationType='query by clinicId', originData=keyword,
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


def alter_prescription_method(id, patientName, sex, age, phoneNum, diagnosis, feature, treatment, doctorId, operatorId):
    originPrescription = Prescription.objects.filter(id=id)
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


def get_image_method(id, ownerType, imageType, operatorId):
    try:
        if not imageType == 'all':
            data = []
            imagePath = os.path.join(settings.UPLOAD_FILE, ownerType, id, imageType)
            for image in os.listdir(imagePath):
                singleImagePath = os.path.join('images', ownerType, id, imageType, image)
                data.append(singleImagePath)

            return JsonResponse({'data': data})
        else:
            qualifications = []
            imagePath = os.path.join(settings.UPLOAD_FILE, ownerType, id, 'qualification')
            for image in os.listdir(imagePath):
                singleImagePath = os.path.join('images', ownerType, id, 'qualification', image)
                qualifications.append(singleImagePath)

            photos = []
            imagePath = os.path.join(settings.UPLOAD_FILE, ownerType, id, 'photo')
            for image in os.listdir(imagePath):
                singleImagePath = os.path.join('images', ownerType, id, 'photo', image)
                photos.append(singleImagePath)

            return JsonResponse({'qualifications': qualifications, 'photos': photos})
    except:
        return JsonResponse({'checkCode': '0'})


def change_user_authority_method(id, usertype, operatorId, changeTo):
    user = []
    if usertype == '1':
        user = Clinic.objects.get(id=id).userId
    elif usertype == '2':
        user = Doctor.objects.get(id=id).userId
    user.authorized = changeTo
    user.save()
    return JsonResponse({'message': '更改授权情况成功'})


def date_type_statistic_method(date, type):
    # day需要+1
    if type == 'mostclinictoday':
        # 今日接诊人次最多的诊所
        currentday = int(date[0][2] + 1)
        prescriptions = Prescription.objects.filter(
            Q(createTime__year=date[0][0]) & Q(createTime__month=date[0][1]) & Q(createTime__day=currentday)).order_by(
            'doctorId__clinicId')
        if prescriptions:
            clinicsid = []
            clinicsname = []
            frequency = []
            clinicsid.append(prescriptions[0].doctorId.clinicId.id)
            clinicsname.append(prescriptions[0].doctorId.clinicId.name)
            frequency.append(1)
            for i in range(1, prescriptions.count()):
                last = len(clinicsid) - 1
                lastclinicid = clinicsid[last]
                clinicid = prescriptions[i].doctorId.clinicId.id
                clinicname = prescriptions[i].doctorId.clinicId.name
                if clinicid == lastclinicid:
                    frequency[last] = frequency[last] + 1
                else:
                    clinicsid.append(prescriptions[i].doctorId.clinicId.id)
                    clinicsname.append(prescriptions[i].doctorId.clinicId.name)
                    frequency.append(1)
                # 显示前5位
                if len(frequency) > 4:
                    break
            return JsonResponse(
                {'message': '今日接诊人次最多诊所', 'clinicsid': clinicsid, 'clinicsname': clinicsname, 'frequency': frequency})
    elif type == '2':
        print(2)
    elif type == '4':
        print(4)
    return JsonResponse({'message': '今日接诊人次最多诊所', 'clinicsid': '', 'clinicsname': '', 'frequency': ''})
