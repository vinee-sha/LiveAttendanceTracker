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
    path('UploadZIP/', views.UploadZIP, name="UploadZIP"),
    path('downloadCSV/', views.downloadCSV, name="downloadCSV"),
    path('downloadZIP/', views.downloadZIP, name="downloadZIP"),
    path('uploadFile/', views.uploadFile, name="uploadFile"),
    path('uploadFolder/', views.uploadFolder, name="uploadFolder"),
]