from django.shortcuts import render,redirect
from django.http import HttpResponse
from sistem.models import *
from sistem.forms import *
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.db.models import Sum
import datetime
import calendar

#OBTENER FECHA ACTUAL Y FORMATEAR SEMANA Y MES ACTUALES
horayfecha = datetime.datetime.now()
semanaactual = horayfecha.isocalendar().week
mesactualnumero = horayfecha.strftime("%m").capitalize()
match mesactualnumero:
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


#######################################################################
# Create your views here.
@login_required
def home(request):
    return render(request, 'index.html' )

def salir(request):
    logout(request)
    return redirect('login.html')

#################### ESTADISTICAS ###################################
def estadisticas(request):

    
    citasmes = Cita.objects.filter(fechacita__month=mesactualnumero).count()
    consultasmes = Consulta.objects.filter(fechaconsulta__month =mesactualnumero).count()
    devengadomes = Consulta.objects.filter(fechaconsulta__month =mesactualnumero).aggregate(Sum('precioconsulta')).get('precioconsulta__sum')

    totalpacientes = Paciente.objects.count()
    consultasles = Consulta.objects.filter(tipo = "Les").count()
    consultaspat = Consulta.objects.filter(tipo = "Pat").count()
    totaldevengado = Consulta.objects.all().aggregate(Sum('precioconsulta')).get('precioconsulta__sum')
    totalcitas = Cita.objects.count()
    totalconsultas = Consulta.objects.count()

    data = {
        'devengadomes': devengadomes,
        'consultasmes': consultasmes,
        'mesactual': mesactual,
        'citasmes': citasmes,

        'totalcitas': totalcitas,
        'totalpacientes': totalpacientes,
        'consultaslesion': consultasles,
        'consultaspat': consultaspat,
        'totaldevengado': totaldevengado,
        'totalconsultas': totalconsultas
    }

    return render(request, 'estadisticas.html', data)

########################### CITAS ##############################################

#VISTA PARA LISTAR CITAS
def ListaCitas(request):

    
    #OBTENCION DE FECHAS DE LA SEMANA
    numerodia = horayfecha.isoweekday()
    match numerodia:
        case 1 : #ES LUNES
            fechalunes = horayfecha.strftime("%d").capitalize()
            fechamartes = (horayfecha + datetime.timedelta(days=1)).strftime("%d").capitalize()
            fechamiercoles = (horayfecha + datetime.timedelta(days=2)).strftime("%d").capitalize()
            fechajueves = (horayfecha + datetime.timedelta(days=3)).strftime("%d").capitalize()
            fechaviernes = (horayfecha + datetime.timedelta(days=4)).strftime("%d").capitalize()
        case 2:#ES MARTES
            fechalunes = (horayfecha - datetime.timedelta(days=1)).strftime("%d").capitalize()
            fechamartes = horayfecha.strftime("%d").capitalize()
            fechamiercoles = (horayfecha + datetime.timedelta(days=1)).strftime("%d").capitalize()
            fechajueves = (horayfecha + datetime.timedelta(days=2)).strftime("%d").capitalize()
            fechaviernes = (horayfecha + datetime.timedelta(days=3)).strftime("%d").capitalize()
        case 3:#ES MIERCOLES
            fechalunes = (horayfecha - datetime.timedelta(days=2)).strftime("%d").capitalize()
            fechamartes = (horayfecha - datetime.timedelta(days=1)).strftime("%d").capitalize()
            fechamiercoles = horayfecha.strftime("%d").capitalize()
            fechajueves = (horayfecha + datetime.timedelta(days=1)).strftime("%d").capitalize()
            fechaviernes = (horayfecha + datetime.timedelta(days=2)).strftime("%d").capitalize()
        case 4:#ES JUEVES
            fechalunes = (horayfecha - datetime.timedelta(days=3)).strftime("%d").capitalize()
            fechamartes = (horayfecha - datetime.timedelta(days=2)).strftime("%d").capitalize()
            fechamiercoles = (horayfecha - datetime.timedelta(days=1)).strftime("%d").capitalize()
            fechajueves = horayfecha.strftime("%d").capitalize()
            fechaviernes = (horayfecha + datetime.timedelta(days=1)).strftime("%d").capitalize()
        case 5:#ES VIERNES
            fechalunes = (horayfecha - datetime.timedelta(days=4)).strftime("%d").capitalize()
            fechamartes = (horayfecha - datetime.timedelta(days=3)).strftime("%d").capitalize()
            fechamiercoles = (horayfecha - datetime.timedelta(days=2)).strftime("%d").capitalize()
            fechajueves = (horayfecha - datetime.timedelta(days=1)).strftime("%d").capitalize()
            fechaviernes = horayfecha.strftime("%d").capitalize()
        case 6:#ES SABADO
            fechalunes = (horayfecha - datetime.timedelta(days=5)).strftime("%d").capitalize()
            fechamartes = (horayfecha - datetime.timedelta(days=4)).strftime("%d").capitalize()
            fechamiercoles = (horayfecha - datetime.timedelta(days=3)).strftime("%d").capitalize()
            fechajueves = (horayfecha - datetime.timedelta(days=2)).strftime("%d").capitalize()
            fechaviernes = (horayfecha - datetime.timedelta(days=1)).strftime("%d").capitalize()
        case 7:#ES DOMINGO
            fechalunes = (horayfecha + datetime.timedelta(days=1)).strftime("%d").capitalize()
            fechamartes = (horayfecha + datetime.timedelta(days=2)).strftime("%d").capitalize()
            fechamiercoles = (horayfecha + datetime.timedelta(days=3)).strftime("%d").capitalize()
            fechajueves = (horayfecha + datetime.timedelta(days=4)).strftime("%d").capitalize()
            fechaviernes = (horayfecha + datetime.timedelta(days=5)).strftime("%d").capitalize()
    
    conteocitas = Cita.objects.filter(fechacita__week = semanaactual).count()

    #FOR QUE CONSULTA LAS CITAS PARA LA HORA DE 8 A 9
    citas1 = []
    citas1.append(1)#AGREGAMOS 1 PARA MOSTRAR LA HORA
    for i in range(2,7):
        citas_1 = Cita.objects.filter(horacita=1, fechacita__week=semanaactual, fechacita__week_day=i)
        if len(citas_1) == 0:
            citas1.append(2)#AGREGAMOS 2 PARA MOSTRAR DISPONIBILIDAD EN LA CITA
        else:
            for cita1 in citas_1: 
                citas1.append(cita1)       
    
    #FOR QUE CONSULTA LAS CITAS PARA LA HORA DE 9 A 10
    citas2 = []
    citas2.append(1)#AGREGAMOS 1 PARA MOSTRAR LA HORA
    for i in range(2,7):
        citas_2 = Cita.objects.filter(horacita=2, fechacita__week=semanaactual, fechacita__week_day=i)
        if len(citas_2) == 0:
            citas2.append(2)#AGREGAMOS 2 PARA MOSTRAR DISPONIBILIDAD EN LA CITA
        else:
            for cita2 in citas_2: 
                citas2.append(cita2)

    #FOR QUE CONSULTA LAS CITAS PARA LA HORA DE 10 A 11
    citas3 = []
    citas3.append(1)#AGREGAMOS 1 PARA MOSTRAR LA HORA
    for i in range(2,7):
        citas_3 = Cita.objects.filter(horacita=3, fechacita__week=semanaactual, fechacita__week_day=i)
        if len(citas_3) == 0:
            citas3.append(2)#AGREGAMOS 2 PARA MOSTRAR DISPONIBILIDAD EN LA CITA
        else:
            for cita3 in citas_3: 
                citas3.append(cita3)

    #FOR QUE CONSULTA LAS CITAS PARA LA HORA DE 11 A 12
    citas4 = []
    citas4.append(1)#AGREGAMOS 1 PARA MOSTRAR LA HORA
    for i in range(2,7):
        citas_4 = Cita.objects.filter(horacita=4, fechacita__week=semanaactual, fechacita__week_day=i)
        if len(citas_4) == 0:
            citas4.append(2)#AGREGAMOS 2 PARA MOSTRAR DISPONIBILIDAD EN LA CITA
        else:
            for cita4 in citas_4: 
                citas4.append(cita4)
    
    #FOR QUE CONSULTA LAS CITAS PARA LA HORA DE 1 A 2
    citas5 = []
    citas5.append(1)#AGREGAMOS 1 PARA MOSTRAR LA HORA
    for i in range(2,7):
        citas_5 = Cita.objects.filter(horacita=5, fechacita__week=semanaactual, fechacita__week_day=i)
        if len(citas_5) == 0:
            citas5.append(2)#AGREGAMOS 2 PARA MOSTRAR DISPONIBILIDAD EN LA CITA
        else:
            for cita5 in citas_5: 
                citas5.append(cita5)

    #FOR QUE CONSULTA LAS CITAS PARA LA HORA DE 2 A 3
    citas6 = []
    citas6.append(1)#AGREGAMOS 1 PARA MOSTRAR LA HORA
    for i in range(2,7):
        citas_6 = Cita.objects.filter(horacita=6, fechacita__week=semanaactual, fechacita__week_day=i)
        if len(citas_6) == 0:
            citas6.append(2)#AGREGAMOS 2 PARA MOSTRAR DISPONIBILIDAD EN LA CITA
        else:
            for cita6 in citas_6: 
                citas6.append(cita6)
    
    #FOR QUE CONSULTA LAS CITAS PARA LA HORA DE 3 A 4
    citas7 = []
    citas7.append(1)#AGREGAMOS 1 PARA MOSTRAR LA HORA
    for i in range(2,7):
        citas_7 = Cita.objects.filter(horacita=7, fechacita__week=semanaactual, fechacita__week_day=i)
        if len(citas_7) == 0:
            citas7.append(2)#AGREGAMOS 2 PARA MOSTRAR DISPONIBILIDAD EN LA CITA
        else:
            for cita7 in citas_7: 
                citas7.append(cita7)
    
    #FOR QUE CONSULTA LAS CITAS PARA LA HORA DE 4 A 5
    citas8 = []
    citas8.append(1)#AGREGAMOS 1 PARA MOSTRAR LA HORA
    for i in range(2,7):
        citas_8 = Cita.objects.filter(horacita=8, fechacita__week=semanaactual, fechacita__week_day=i)
        if len(citas_8) == 0:
            citas8.append(2)#AGREGAMOS 2 PARA MOSTRAR DISPONIBILIDAD EN LA CITA
        else:
            for cita8 in citas_8: 
                citas8.append(cita8)

    #FOR QUE CONSULTA LAS CITAS PARA LA HORA DE 5 A 6
    citas9 = []
    citas9.append(1)#AGREGAMOS 1 PARA MOSTRAR LA HORA
    for i in range(2,7):
        citas_9 = Cita.objects.filter(horacita=9, fechacita__week=semanaactual, fechacita__week_day=i)
        if len(citas_9) == 0:
            citas9.append(2)#AGREGAMOS 2 PARA MOSTRAR DISPONIBILIDAD EN LA CITA
        else:
            for cita9 in citas_9: 
                citas9.append(cita9)

    data = {
        'fechalunes': fechalunes,
        'fechamartes': fechamartes,
        'fechamiercoles': fechamiercoles,
        'fechajueves': fechajueves,
        'fechaviernes': fechaviernes,
        'citas1': citas1,
        'citas2': citas2,
        'citas3': citas3,
        'citas4': citas4,
        'citas5': citas5,
        'citas6': citas6,
        'citas7': citas7,
        'citas8': citas8,
        'citas9': citas9,
        'conteocitas':conteocitas,
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
            #CONSULTA LA INFORMACION DEL FORM
            fecha = form.cleaned_data['fechacita']
            dia = fecha.isoweekday()
            hora = form.cleaned_data['horacita']
            #CONSULTA SI EXISTE LA CITA EN LA BASE
            cita = Cita.objects.filter(horacita=hora, fechacita=fecha)
            if len(cita) == 1: 
                print('Cita ya existe')
                return render(
                request,
                'Citas/crear_cita.html',
                {'CitaForm': form})
            else:
                print('Cita creada')
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


########################## PACIENTES ################################################

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


########################### CONSULTAS ###############################################

#VISTA PARA LISTAR CONSULTAS
def ListaConsultas(request):
    consultas = Consulta.objects.all().order_by('-idconsulta')
    pagina = request.GET.get("page", 1)

    try:
        paginator = Paginator(consultas, 10)
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


############################ USUARIOS ##############################################

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