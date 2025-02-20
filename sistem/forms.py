from django import forms
from sistem.models import *


class DateInput(forms.DateInput):
    input_type = 'date'
    
class PacienteForm(forms.ModelForm):

    class Meta:
        model = Paciente
        fields = '__all__'
        widgets = {
            'fecha_nacimiento':DateInput(
                attrs= {
                     'class':'form-control',
                    'placeholder':'AÑO/MES/DIA'
                }
            )
        }
        
class ConsultaForm(forms.ModelForm):

    class Meta:
        model = Consulta
        fields = '__all__'

class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = '__all__'

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = '__all__'
        widgets = {
            'fechacita':DateInput(
                attrs= {
                     'class':'form-control',
                    'placeholder':'MES/DIA/AÑO'
                }
            )
        }