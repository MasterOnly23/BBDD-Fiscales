from tkinter.font import families
from django import forms
from fiscales.models import Fiscales


class Formularios(forms.ModelForm):
    
    class Meta:
        model = Fiscales
        fields = '__all__'
        widgets = {'fecha_cambio': forms.DateInput(attrs={'type':'date'})} #por el campo de fehc ade nacimiento


