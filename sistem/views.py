from django.shortcuts import render,redirect
from django.http import HttpResponse
from sistem.models import *
from sistem.forms import *
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import datetime

# Create your views here.
@login_required
def home(request):
    return render(request, 'index.html' )

def salir(request):
    logout(request)
    return redirect('login.html')
#########################################################################
'''#OBTENER FECHA
    horayfecha = datetime.datetime.now()
    fha = horayfecha
    mesactual = fha.strftime("%M").capitalize()
    match mesactual:
        case "01" :
            mesactual ="Enero" 
        case "02":
            mesactual ="Febrero" 
        case "03":
            mesactual ="Marzo"
        case "04" :
            mesactual ="Abril" 
        case "05":
            mesactual ="Mayo" 
        case "06":
            mesactual ="Junio" 
        case "07" :
            mesactual ="Julio" 
        case "08":
            mesactual ="Agosto" 
        case "09":
            mesactual ="Septiembre"
        case "10" :
            mesactual ="Octubre" 
        case "11":
            mesactual ="Noviembre" 
        case "12":
            mesactual ="Diciembre" '''



#VISTA PARA LISTAR CITAS
def ListaCitas(request):

    #VARIABLE PARA MOSTRAR LAS HORAS EN LA TABLA DE LA VISTA
    horario = ['08:00 - 09:00','09:00 - 10:00','10:00 - 11:00','11:00 - 12:00',
               '01:00 - 02:00','02:00 - 03:00','03:00 - 04:00','04:00 - 05:00',
               '05:00 - 06:00']
    
    #OBTENER FECHA ACTUAL Y AISLAR SEMANA Y MES ACTUALES
    horayfecha = datetime.datetime.now()
    semanaactual = horayfecha.isocalendar().week
    fha = horayfecha
    mesactual = fha.strftime("%m").capitalize()

    
    #FOR QUE CONSULTA LAS CITAS PARA EL DIA LUNES
    citaslunes = [] 
    for i in range(1,10):
        citas_lunes = Cita.objects.filter(horacita=i, fechacita__week=semanaactual)    
        if len(citas_lunes) == 0:
            print('disponible')
            citaslunes.append('disponible')
        else:
            for lunes in citas_lunes:
                fecha = lunes.fechacita
                #semana = fecha.isocalendar().week
                dia = fecha.isoweekday()

                if dia != 1:
                    print(dia)
                    citaslunes.append('disponible')
                else:
                    citaslunes.append(lunes)
                
                    
    #FOR QUE CONSULTA LAS CITAS PARA EL DIA MARTES
    citasmartes = [] 
    for i in range(1,10):
        citas_martes = Cita.objects.filter(horacita=i, fechacita__week=semanaactual)    
        if len(citas_martes) == 0:
            #print(i)
            citasmartes.append('disponible')
        else:
            for martes in citas_martes:
                fecha = martes.fechacita
                dia = fecha.isoweekday()
                
                if dia != 2:
                    #print(martes)
                    citasmartes.append('disponible')
                else:
                    citasmartes.append(martes)

    
    match mesactual:
        case "01" :
            mesactual ="Enero" 
        case "02":
            mesactual ="Febrero" 
        case "03":
            mesactual ="Marzo"
        case "04" :
            mesactual ="Abril" 
        case "05":
            mesactual ="Mayo" 
        case "06":
            mesactual ="Junio" 
        case "07" :
            mesactual ="Julio" 
        case "08":
            mesactual ="Agosto" 
        case "09":
            mesactual ="Septiembre"
        case "10" :
            mesactual ="Octubre" 
        case "11":
            mesactual ="Noviembre" 
        case "12":
            mesactual ="Diciembre" 
    
    data = {
        'horario': horario,
        'citaslunes': citaslunes,
        'citasmartes': citasmartes,
        'mes':mesactual,
        'semana': semanaactual
    }
    return render(request, 'Citas/citas.html',data)



#VISTA PARA AGREGAR CITA
def crear_cita(request):
    if request.method == 'GET':
        return render(
            request,
            'Citas/crear_cita.html',
            {'CitaForm': CitaForm}
        )
    if request.method == 'POST':
        form = CitaForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/citas/')
        else:
            form = CitaForm(data=request.POST)
            return render(
                request,
                'Citas/crear_cita.html',
                {'CitaForm': form}
            )
#VISTA EDITAR CITA
def editar_cita(request, pk=None):
    cita = Cita.objects.get(pk=pk)

    if request.method == 'GET':
        citaform=CitaForm(instance=cita)

        return render(
            request,
            'Citas/actualizar_cita.html',
            {
                'cita': cita, 
                'citaform':citaform
            }
        )
    if request.method == 'POST':
        citaform=CitaForm(
            data=request.POST,
            instance=cita
        )
        if citaform.is_valid():
            citaform.save()
            return redirect('/citas/')
        else:
            citaform=CitaForm(
            data=request.POST,
            instance=cita
        )
        return render(
            request,
            'Citas/crear_cita.html',
            {'CitaForm': citaform}
        )
#VISTA ELIMINAR CITAS
def eliminar_cita(request, pk=None):
    Cita.objects.filter(pk=pk).delete()
    return redirect('/citas/')

##########################################################################

#VISTA LISTAR PACIENTES
def ListaPacientes(request):
    pacientes = Paciente.objects.all().order_by('-idpaciente')
    pagina = request.GET.get("page", 1)

    try:
        paginator = Paginator(pacientes, 7)
        pacientes = paginator.page(pagina)
    except:
        raise Http404

    data = {
        'entity': pacientes,
        'paginator':paginator

    }
    return render(request, 'Pacientes/pacientes.html',data )

#VISTA CREAR PACIENTE
def crear_paciente(request):
    if request.method == 'GET':
        return render(
            request,
            'Pacientes/crear_paciente.html',
            {'PacienteForm': PacienteForm}
        )
    if request.method == 'POST':
        form = PacienteForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/pacientes/')
        else:
            form = PacienteForm(data=request.POST)
            return render(
                request,
                'Pacientes/crear_paciente.html',
                {'PacienteForm': form}
            )
#VISTA EDITAR PACIENTE
def editar_paciente(request, pk=None):
    paciente = Paciente.objects.get(pk=pk)

    if request.method == 'GET':
        pacienteform=PacienteForm(instance=paciente)

        return render(
            request,
            'Pacientes/actualizar_paciente.html',
            {
                'paciente': paciente, 
                'pacienteform':pacienteform
            }
        )
    if request.method == 'POST':
        pacienteform=PacienteForm(
            data=request.POST,
            instance=paciente
        )
        if pacienteform.is_valid():
            pacienteform.save()
            return redirect('/pacientes/')
        else:
            pacienteform=PacienteForm(
            data=request.POST,
            instance=paciente
        )
        return render(
            request,
            'Pacientes/crear_paciente.html',
            {'PacienteForm': pacienteform}
        )
#VISTA ELIMINAR PACIENTE
def eliminar_paciente(request, pk=None):
    Paciente.objects.filter(pk=pk).delete()
    return redirect('/pacientes/')

##########################################################################


#VISTA PARA LISTAR CONSULTAS
def ListaConsultas(request):
    consultas = Consulta.objects.all().order_by('-idconsulta')
    pagina = request.GET.get("page", 1)

    try:
        paginator = Paginator(consultas, 2)
        consultas = paginator.page(pagina)
    except:
        raise Http404

    data = {
        'entity': consultas,
        'paginator':paginator
    }
    return render(request,  'Consultas/consultas.html',data )

#VISTA PARA AGREGAR CONSULTAS
def crear_consulta(request):
    if request.method == 'GET':
        return render(
            request,
            'Consultas/crear_consulta.html',
            {'ConsultaForm': ConsultaForm}
        )
    if request.method == 'POST':
        form = ConsultaForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/consultas/')
        else:
            form = ConsultaForm(data=request.POST)
            return render(
                request,
                'Consultas/crear_consulta.html',
                {'ConsultaForm': form}
            )
#VISTA EDITAR COSULTAS
def editar_consulta(request, pk=None):
    consulta = Consulta.objects.get(pk=pk)

    if request.method == 'GET':
        consultaform=ConsultaForm(instance=consulta)

        return render(
            request,
            'Consultas/actualizar_consulta.html',
            {
                'consulta': consulta, 
                'consultaform':consultaform
            }
        )
    if request.method == 'POST':
        consultaform=ConsultaForm(
            data=request.POST,
            instance=consulta
        )
        if consultaform.is_valid():
            consultaform.save()
            return redirect('/consultas/')
        else:
            consultaform=ConsultaForm(
            data=request.POST,
            instance=consulta
        )
        return render(
            request,
            'Consultas/crear_consulta.html',
            {'ConsultaForm': consultaform}
        )
#VISTA ELIMINAR CONSULTAS
def eliminar_consulta(request, pk=None):
    Consulta.objects.filter(pk=pk).delete()
    return redirect('/consultas/')

##########################################################################


#VISTA PARA LISTAR USUARIOS
def ListaUsuarios(request):
    usuarios = Usuario.objects.all().order_by('-idusuario')
    pagina = request.GET.get("page", 1)

    try:
        paginator = Paginator(usuarios, 2)
        usuarios = paginator.page(pagina)
    except:
        raise Http404

    data = {
        'entity': usuarios,
        'paginator':paginator
    }
    return render(request,   'Usuarios/usuarios.html',data )


#VISTA PARA AGREGAR USUARIOS
def crear_usuario(request):
    if request.method == 'GET':
        return render(
            request,
            'Usuarios/crear_usuario.html',
            {'UsuarioForm': UsuarioForm}
        )
    if request.method == 'POST':
        form = UsuarioForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/usuarios/')
        else:
            form = UsuarioForm(data=request.POST)
            return render(
                request,
                'Usuarios/crear_usuario.html',
                {'UsuarioForm': form}
            )

#VISTA EDITAR USUARIOS
def editar_usuario(request, pk=None):
    usuario = Usuario.objects.get(pk=pk)

    if request.method == 'GET':
        usuarioform=UsuarioForm(instance=usuario)

        return render(
            request,
            'Usuarios/actualizar_usuario.html',
            {
                'usuario': usuario, 
                'usuarioform':usuarioform
            }
        )
    if request.method == 'POST':
        usuarioform=UsuarioForm(
            data=request.POST,
            instance=usuario
        )
        if usuarioform.is_valid():
            usuarioform.save()
            return redirect('/usuarios/')
        else:
            usuarioform=UsuarioForm(
            data=request.POST,
            instance=usuario
        )
        return render(
            request,
            'Usuarios/actualizar_usuario.html',
            {'usuario': usuario,
             'usuarioform': usuarioform}
        )

#VISTA ELIMINAR USUARIOS
def eliminar_usuario(request, pk=None):
    Usuario.objects.filter(pk=pk).delete()
    return redirect('/usuarios/')