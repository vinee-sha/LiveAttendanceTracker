from .models import uploadFile
from django import forms

class uploadfileform(forms.ModelForm):
    	class Meta:
            model=uploadFile
            fields=('File_to_upload',)