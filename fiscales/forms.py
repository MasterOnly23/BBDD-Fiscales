from dataclasses import fields
from tkinter.font import families
from django import forms
from fiscales.models import Fiscales, Backups


class Formularios(forms.ModelForm):
    
    class Meta:
        model = Fiscales
        fields = '__all__'
        widgets = {'fecha_cambio': forms.DateInput(attrs={'type':'date'}), 'vencimiento_certificado_digital': forms.DateInput(attrs={'type':'date'})} #por el campo de fehc ade nacimiento


# class Formularios_bkp(forms.ModelForm):

#     class Meta():
#         model = Backups
#         fields = '__all__'
#         widgets =