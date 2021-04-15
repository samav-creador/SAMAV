from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView, ListView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from noAbandono.admin import UserCreateForm
#from core.models import Server, FileToBackup, Result, ServerGroup 
from .models import *
from .forms import  *
from django.db import connection as db
from django.core import serializers


# Create your views here.

def home(request):
    return render(request, "index.html")

def logout_request(request):
    logout(request)
    return redirect("index")

def index(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, "Usuario y/o cotraseña erroneos")
        else:
            messages.error(request, "Usuario y/o cotraseña erroneos")
    form = AuthenticationForm()
    return render(request = request, template_name = "login.html")

def register(request):
    # Creamos el formulario de autenticación vacío
    form = UserCreateForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = UserCreateForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():

            # Creamos la nueva cuenta de usuario
            user = form.save()

            # Si el usuario se crea correctamente 
            if user is not None:
                # Hacemos el login manualmente
                login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')
    form.fields['username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None

    # Si llegamos al final renderizamos el formulario
    return render(request, "register.html", {'form': form})

#### Grupos ####

class GruposListView(ListView):
    model = Grupo
    template_name = 'grupolist.html'

class GrupoCreateView(CreateView):
    model = Grupo
    form_class = GrupoForm
    template_name = 'grupo.html'
    success_url='listGrupo'

#### Alumnos ####

class AlumnosListView(ListView):
    model = Alumno
    template_name = 'alumnolist.html'

class AlumnoCreateView(CreateView):
    model = Alumno
    form_class = AlumnoForm
    template_name = 'alumno.html'
    success_url='listAlumno'

#### Materias ####

class MateriasListView(ListView):
    model = Materia
    template_name = 'materialist.html'

class MateriaCreateView(CreateView):
    model = Materia
    form_class = MateriaForm
    template_name = 'materia.html'
    success_url='listMateria'

#### Problemáticas ####

def reportes(request):
    return render(request, "reportes.html")

def reportesFechas(request):
    return render(request, "reportesFechas.html")

def reportesAlumnos(request):
    return render(request, "reportesAlumnos.html")

def reportesGrupos(request):
    return render(request, "reportesGrupos.html")

def fechaRep(request):
    fecha = request.GET.get('fecha')
    lista = Problematica.objects.filter(fecha = fecha)
    context = {'lista':lista}
    return render(request, "reporteFecha.html", context)

def RepAlum(request):
    nombre = request.GET.get('nombre')
    id_al = Alumno.objects.filter(nombre__contains = nombre)[0]
    lista = Problematica.objects.filter(alumno = id_al)
    context = {'lista':lista}
    return render(request, "reporteAlumno.html", context)

def RepGpo(request):
    gpo = request.GET.get('nombre')
    id_gpo = Grupo.objects.get(nombre = gpo)
    lista = Problematica.objects.filter(grupo = id_gpo)
    context = {'lista':lista}
    return render(request, "reporteGrupo.html", context)

class ProblematicasListView(ListView):
    model = Problematica
    paginate_by = 10
    template_name = 'problematicalist.html'

class ProblematicaCreateView(CreateView):
    model = Problematica
    form_class = ProblematicaForm
    template_name = 'problematica.html'
    success_url='listProblematica'

class ProblematicaUpdateView(UpdateView):
    model = Problematica
    form_class = ProblematicaForm
    template_name = 'problematica_form.html'

    def get_context_data(self, **kwargs):
        context = super(ProblematicaUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['problematica'] = ProblematicaForm(self.request.POST, instance = self.object)
        else:
            context['problematica'] = ProblematicaForm(instance = self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data(form = form)
        problematica = context['problematica']
        if problematica.is_valid():
            self.object = form.save()
            problematica = problematica.save
            return HttpResponseRedirect(reverse('listProblematica'))
        else:
            return self.render_to_response(self.get_context_data(form = form))

def llenaAl(request):
    grupo = request.GET.get('gpo')
    alumnos = Alumno.objects.all().values('id','nombre').filter(grupo = str(grupo))
    return render(request,"llenaAl.html",{'alumnos':alumnos})

def llenaMat(request):
    grupo = request.GET.get('gpo')
    materias = Materia.objects.all().values('id','nombre').filter(grupo = str(grupo))
    return render(request,"llenaMat.html",{'materias':materias})
