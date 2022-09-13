from tkinter.font import families
from django import forms
from familiares.models import Familiares


class Formularios(forms.ModelForm):
    
    class Meta:
        model = Familiares
        fields = '__all__'
        widgets = {'fecha_nacimiento': forms.DateInput(attrs={'type':'date'})} #por el campo de fehc ade nacimiento


