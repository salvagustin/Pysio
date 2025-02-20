from django.contrib import admin
from .models import Paciente
from .models import Usuario
from .models import Consulta

# Register your models here.
admin.site.register(Paciente)
admin.site.register(Usuario)
admin.site.register(Consulta)