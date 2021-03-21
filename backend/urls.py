from django.urls import path, include
from backend import views

urlpatterns = [
    path('login/', views.login),
    path('add_user/', views.add_user),
    path('delete_user/', views.delete_user),
    path('show_user/', views.show_user),
    path('query_user/', views.query_user),
    path('alter_user/', views.alter_user),
    path('add_doctor/', views.add_doctor),
    path('delete_doctor/', views.delete_doctor),
    path('show_doctor/', views.show_doctor),
    path('query_doctor/', views.query_doctor),
    path('alter_doctor/', views.alter_doctor),
    path('add_clinic/', views.add_clinic),
    path('delete_clinic/', views.delete_clinic),
    path('show_clinic/', views.show_clinic),
    path('query_clinic/', views.query_clinic),
    path('alter_clinic/', views.alter_clinic),
    path('add_prescription/', views.add_prescription),
    path('delete_prescription/', views.delete_prescription),
    path('show_prescription/', views.show_prescription),
    path('query_prescription/', views.query_prescription),
    path('alter_prescription/', views.alter_prescription),
]
