from django.forms import ModelForm
from django import forms
from .models import * 
from django.core.exceptions import ValidationError

class HardwareForm(ModelForm):
    def __init__(self, *args, **kwargs):
         super(HardwareForm, self).__init__(*args, **kwargs) 
         self.fields['tipo'].widget.attrs = {
            'id':'tipo',
            'class':'form-control',
        }
         self.fields['marca'].widget.attrs = {
            'id':'marca',
            'class':'form-control',
        }
         self.fields['modelo'].widget.attrs = {
            'id':'modelo',
            'class':'form-control',
        }
         self.fields['nro_de_serie'].widget.attrs = {
            'id':'nro_de_serie',
            'class':'form-control',
            'placeholder':'Ingresar numero de serie...'
        }
         self.fields['ubicacion'].widget.attrs = {
            'id':'ubicacion',
            'class':'form-control',
            'placeholder':'Ingrese ubicacion'
        }
         self.fields['estado'].widget.attrs = {
            'id':'estado',
            'class':'form-control',
        }
         self.fields['origen'].widget.attrs = {
             'id':'origen',
            'class':'form-control',
            'style':"resize: none;",
            'rows':"10",
            'required':False
         }
         self.fields['nota'].widget.attrs = {
            'id':'nota',
            'class':'form-control',
            'style':"resize: none;",
            'rows':"3",
            'required':False
        }
         self.fields['observaciones'].widget.attrs = {
            'id':'observaciones',
            'class':'form-control',
            'style':"resize: none;",
            'rows':"10",
            'required':False
        }
         
         
    

    class Meta:
        model = Hardware
        fields="__all__"

class HardwareEditForm(ModelForm):
    def __init__(self, *args, **kwargs):
         
         super(HardwareEditForm, self).__init__(*args, **kwargs) 
         self.fields['tipo'].widget.attrs = {
            'id':'tipo',
            'class':'form-control', 
        }
         self.fields['marca'].widget.attrs = {
            'id':'marca',
            'class':'form-control',
        }
         self.fields['modelo'].widget.attrs = {
            'id':'modelo',
            'class':'form-control',
        }
         self.fields['nro_de_serie'].widget.attrs = {
            'id':'nro_de_serie',
            'class':'form-control',
            'placeholder':'Ingresar numero de serie...',
            
        }
         self.fields['ubicacion'].widget.attrs = {
            'id':'ubicacion',
            'class':'form-control',
            'placeholder':'Ingrese ubicacion'
        }
         self.fields['estado'].widget.attrs = {
            'id':'estado',
            'class':'form-control',
        }
         self.fields['origen'].widget.attrs = {
             'id':'origen',
            'class':'form-control',
            'style':"resize: none;",
            'rows':"10",
            'required':False
         }
         self.fields['nota'].widget.attrs = {
            'id':'nota',
            'class':'form-control',
            'style':"resize: none;",
            'rows':"3",
            'required':False
        }
         self.fields['observaciones'].widget.attrs = {
            'id':'observaciones',
            'class':'form-control',
            'style':"resize: none;",
            'rows':"10",
            'required':False
        }
        
         
    class Meta:
        model = Hardware
        fields="__all__"


class CambioContraseñaForm(forms.Form):
    nueva_contraseña = forms.CharField(widget=forms.PasswordInput)
    confirmar_contraseña = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        nueva_contraseña = cleaned_data.get('nueva_contraseña')
        confirmar_contraseña = cleaned_data.get('confirmar_contraseña')

        if nueva_contraseña and confirmar_contraseña and nueva_contraseña != confirmar_contraseña:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return cleaned_data
