from django import forms
from sistem.models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class PacienteForm(forms.ModelForm):

    class Meta:
        model = Paciente
        fields = '__all__'       
        widgets = {'fecha_nacimiento':DateInput(),
                   'nombre': forms.TextInput(attrs={'placeholder': 'Nombre'}),
                   'telefono': forms.TextInput(attrs={'placeholder': 'XXXX XXXX'})
                   
                   }



class ConsultaForm(forms.ModelForm):

    class Meta:
        model = Consulta
        fields = '__all__'
        widgets = {'observaciones':forms.Textarea(attrs={'placeholder': 'Detalles de la consulta',"rows":5}),
                   'precioconsulta':forms.TextInput(attrs={'placeholder': '$00.00'})
                   
                   }

class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = '__all__'

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = '__all__'
        widgets = {'fechacita':DateInput(attrs= {'class':'form-control'}),
                    'observaciones':forms.Textarea(attrs={'placeholder': 'Detalles de la cita'})
                   
                   }