from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('StudentLogin/', views.StudentLogin, name="StudentLogin"),
    path('TeacherLogin/', views.TeacherLogin, name="TeacherLogin"),
    path('StudentRegister/', views.StudentRegister, name="StudentRegister"),
    path('TeacherRegister/', views.TeacherRegister, name="TeacherRegister"),
    path('StudentLoginSubmit/', views.StudentLoginSubmit, name="StudentLoginSubmit"),
    path('TeacherLoginSubmit/', views.TeacherLoginSubmit, name="TeacherLoginSubmit"),
    path('StudentRegisterSubmit/', views.StudentRegisterSubmit, name="StudentRegisterSubmit"),
    path('TeacherRegisterSubmit/', views.TeacherRegisterSubmit, name="TeacherRegisterSubmit"),
    path('TeacherEdit/', views.TeacherEdit, name="TeacherEdit"),
    path('TeacherEditSubmit/', views.TeacherEditSubmit, name="TeacherEditSubmit"),
    path('StudentEdit/', views.StudentEdit, name="StudentEdit"),
    path('StudentEditSubmit/', views.StudentEditSubmit, name="StudentEditSubmit"),
    path('ForgotPassword/', views.ForgotPassword, name="ForgotPassword"),
    path('ForgotPasswordSubmit/', views.ForgotPasswordSubmit, name="ForgotPasswordSubmit"),
]