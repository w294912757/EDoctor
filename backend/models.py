from django.db import models


class Clinic(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, blank=False, null=False)
    department = models.CharField(max_length=20, blank=False, null=False)
    address = models.CharField(max_length=20, blank=False, null=False)
    phoneNum = models.CharField(max_length=20, blank=False, null=False)
    userId = models.ForeignKey("User", to_field="id", on_delete=models.DO_NOTHING, default='')
    createTime = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updateTime = models.DateTimeField(auto_now=True, null=True, blank=True)


class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, blank=False, null=False)
    department = models.CharField(max_length=20, blank=False, null=False)
    sex = models.CharField(max_length=10, blank=False, null=False)
    age = models.CharField(max_length=10, blank=False, null=False)
    userId = models.ForeignKey("User", to_field="id", on_delete=models.DO_NOTHING, default='')
    clinicId = models.ForeignKey("Clinic", to_field="id", on_delete=models.DO_NOTHING, default='')
    createTime = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updateTime = models.DateTimeField(auto_now=True, null=True, blank=True)


class Prescription(models.Model):
    id = models.AutoField(primary_key=True)
    patientName = models.CharField(max_length=20, blank=False, null=False)
    sex = models.CharField(max_length=10, blank=False, null=False)
    age = models.CharField(max_length=10, blank=False, null=False)
    phoneNum = models.CharField(max_length=20, blank=False, null=False)
    diagnosis = models.CharField(max_length=20, blank=False, null=False)
    feature = models.CharField(max_length=20, blank=False, null=False)
    treatment = models.CharField(max_length=20, blank=False, null=False)
    doctorId = models.ForeignKey("Doctor", to_field="id", on_delete=models.DO_NOTHING, default='')
    createTime = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updateTime = models.DateTimeField(auto_now=True, null=True, blank=True)


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, blank=False, null=False)
    password = models.CharField(max_length=20, blank=False, null=False)
    # 用户类型：未指明0 诊所管理1 医生2 系统管理3
    usertype = models.CharField(max_length=5, blank=False, null=False)
    createTime = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updateTime = models.DateTimeField(auto_now=True, null=True, blank=True)


class ClinicLog(models.Model):
    id = models.AutoField(primary_key=True)
    dataId = models.CharField(max_length=20, blank=False, null=False)
    operationType = models.CharField(max_length=20, blank=False, null=False)
    originData = models.CharField(max_length=255, blank=False, null=False)
    resultData = models.CharField(max_length=255, blank=False, null=False)
    operatorId = models.CharField(max_length=20, blank=False, null=False)
    createTime = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updateTime = models.DateTimeField(auto_now=True, null=True, blank=True)


class DoctorLog(models.Model):
    id = models.AutoField(primary_key=True)
    dataId = models.CharField(max_length=20, blank=False, null=False)
    operationType = models.CharField(max_length=20, blank=False, null=False)
    originData = models.CharField(max_length=255, blank=False, null=False)
    resultData = models.CharField(max_length=255, blank=False, null=False)
    operatorId = models.CharField(max_length=20, blank=False, null=False)
    createTime = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updateTime = models.DateTimeField(auto_now=True, null=True, blank=True)


class PrescriptionLog(models.Model):
    id = models.AutoField(primary_key=True)
    dataId = models.CharField(max_length=20, blank=False, null=False)
    operationType = models.CharField(max_length=20, blank=False, null=False)
    originData = models.CharField(max_length=255, blank=False, null=False)
    resultData = models.CharField(max_length=255, blank=False, null=False)
    operatorId = models.CharField(max_length=20, blank=False, null=False)
    createTime = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updateTime = models.DateTimeField(auto_now=True, null=True, blank=True)


class UserLog(models.Model):
    id = models.AutoField(primary_key=True)
    dataId = models.CharField(max_length=20, blank=False, null=False)
    operationType = models.CharField(max_length=20, blank=False, null=False)
    originData = models.CharField(max_length=255, blank=False, null=False)
    resultData = models.CharField(max_length=255, blank=False, null=False)
    operatorId = models.CharField(max_length=20, blank=False, null=False)
    createTime = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updateTime = models.DateTimeField(auto_now=True, null=True, blank=True)
