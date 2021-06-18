from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Home"),
    path('Home/', views.index, name="Home"),
    path('IN/', views.IN, name="IN"),
    path('OUT/', views.OUT, name="OUT"),
    path('Login/', views.Login, name="Login"),
    path('LoginSubmit/', views.LoginSubmit, name="LoginSubmit"),
    path('UploadCSV/', views.UploadCSV, name="UploadCSV"),
    path('UploadImages/', views.UploadImages, name="UploadImages"),
    path('downloadCSV/', views.downloadCSV, name="downloadCSV"),
    path('deleteImages/', views.deleteImages, name="deleteImages"),
    path('uploadFile/', views.uploadFile, name="uploadFile"),
    path('uploadFiles/', views.uploadFiles, name="uploadFiles"),
    path('deleteFiles/', views.deleteFiles, name="deleteFiles"),
    path('regdNoSubmit/', views.regdNoSubmit, name="regdNoSubmit"),
    path('dateSubmit/', views.dateSubmit, name="dateSubmit"),
]