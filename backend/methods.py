import os

from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse

from EDoctor import settings
from backend.models import *
from django.db.models import Q


def login_method(username, password):
    try:
        result = User.objects.get(username=username)
    except ObjectDoesNotExist:
        # 用户不存在
        return JsonResponse({'checkCode': '1'})
    else:
        if password == result.password:
            # 登陆成功
            operatorId = result.id
            usertype = result.usertype
            # 称呼
            title = ''
            if usertype == '1':
                title = Clinic.objects.get(userId=operatorId).name
            elif usertype == '2':
                title = Doctor.objects.get(userId=operatorId).name
            elif usertype == '3':
                title = User.objects.get(id=operatorId).username
            UserLog.objects.create(dataId=operatorId, operationType='login', originData='', resultData='',
                                   operatorId=operatorId)
            rst = {'checkCode': '2', 'title': title}
            response = JsonResponse(rst)
            response.set_cookie('operatorId', operatorId)
            response.set_cookie('usertype', usertype)
            return response
        else:
            # 密码错误
            return JsonResponse({'checkCode': '3'})


def add_user_method(username, password, usertype, operatorId, image):
    try:
        result = User.objects.get(username=username)
    except ObjectDoesNotExist:

        User.objects.create(username=username, password=password, usertype=usertype)
        latestUserId = User.objects.latest('id').id
        imagePath = ''
        if (usertype == '1'):
            imagePath = os.path.join(settings.UPLOAD_FILE, 'clinics', str(latestUserId))
        else:
            imagePath = os.path.join(settings.UPLOAD_FILE, 'doctors', str(latestUserId))
        os.makedirs(imagePath)
        imageFilename = os.path.join(imagePath, image.name)
        f = open(imageFilename, 'wb')
        for i in image.chunks():
            f.write(i)
        f.close()

        resultData = 'username:' + username + ' password:' + password + ' usertype:' + usertype
        operationType = 'add'
        if operatorId == '':
            operationType = 'signUp'
        UserLog.objects.create(dataId=latestUserId, operationType=operationType, originData='',
                               resultData=resultData,
                               operatorId=operatorId)

        return JsonResponse({'message': '用户添加成功'})

    else:
        return JsonResponse({'checkCode': '3'})


def delete_user_method(id, operatorId):
    user = User.objects.get(id=id)
    user.delete()
    UserLog.objects.create(dataId=id, operationType='delete id:', originData=id, resultData='',
                           operatorId=operatorId)
    return JsonResponse({'message': '用户删除成功'})


def show_user_method():
    users = User.objects.all()
    data = []
    for i in users:
        user = {}
        # 给字典添加键值对
        user['id'] = i.id
        user['username'] = i.username
        user['password'] = i.password
        data.append(user)
    return JsonResponse({'message': '查询成功', 'data': data})


def query_user_method(keyword, searchtype, operatorId):
    data = {}
    if searchtype == 'id':
        try:
            result = User.objects.get(id=keyword)
        except ObjectDoesNotExist:
            return JsonResponse({'message': '查询对象结果为空'})

        else:
            # 给字典添加键值对
            data['id'] = result.id
            data['username'] = result.username
            data['password'] = result.password
            data['usertype'] = result.usertype
        UserLog.objects.create(dataId=keyword, operationType='query by id', originData=keyword, resultData='',
                               operatorId=operatorId)
        return JsonResponse({'message': '查询成功', 'data': data})

    if searchtype == 'username':
        try:
            result = User.objects.get(username=keyword)
        except ObjectDoesNotExist:
            return JsonResponse({'message': '查询对象结果为空'})

        else:
            # 给字典添加键值对
            data['id'] = result.id
            data['username'] = result.username
            data['password'] = result.password
            data['usertype'] = result.usertype
        UserLog.objects.create(dataId=result.id, operationType='query by username', originData=keyword, resultData='',
                               operatorId=operatorId)
        return JsonResponse({'message': '查询成功', 'data': data})


def alter_user_method(id, username, password, operatorId):
    originUser = User.objects.get(id=id)
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
    user = User.objects.get(id=userId)
    Clinic.objects.create(name=name, address=address, phoneNum=phoneNum, userId=user, department=department)
    latestClinicId = Clinic.objects.latest('id').id
    resultData = 'name:' + name + ' department:' + department + ' address:' + address + ' phoneNum:' + phoneNum
    ClinicLog.objects.create(dataId=latestClinicId, operationType='add', originData='', resultData=resultData,
                             operatorId=operatorId)
    return JsonResponse({'message': '诊所添加成功'})


def delete_clinic_method(id, operatorId):
    clinic = Clinic.objects.get(id=id)
    clinic.delete()
    ClinicLog.objects.create(dataId=id, operationType='delete id:', originData=id, resultData='',
                             operatorId=operatorId)
    return JsonResponse({'message': '诊所删除成功'})


def show_clinic_method():
    clinics = Clinic.objects.all()
    data = []
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
    return JsonResponse({'message': '查询成功', 'data': data})


def query_clinic_method(keyword, searchtype, operatorId):
    data = {}
    if searchtype == 'id':
        try:
            result = Clinic.objects.get(id=keyword)
        except ObjectDoesNotExist:
            return JsonResponse({'message': '查询对象结果为空'})

        else:
            # 给字典添加键值对
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
    originClinic = Clinic.objects.get(id=id)
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
    resultData = 'name:' + name + 'department:' + department + ' sex:' + sex + ' age:' + age + ' userId:' + userId + ' clinicId:' + clinicId
    DoctorLog.objects.create(dataId=latestDoctorId, operationType='add', originData='', resultData=resultData,
                             operatorId=operatorId)
    return JsonResponse({'message': '医生添加成功'})
