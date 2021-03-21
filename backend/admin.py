from django.contrib import admin
from backend.models import *

admin.site.register([Clinic, Doctor, Prescription,User])

