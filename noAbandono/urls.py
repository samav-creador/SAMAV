"""SAMAV URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, reverse
from django.contrib.auth.decorators import login_required
from .views import *


urlpatterns = [
	path('', login_required(home), name='index'),
    path('accounts/logout/', login_required(logout_request), name='milogout'),
    path('accounts/login/', index , name='index'),
    path('register', register),
	#Grupo
	path('listGrupo', GruposListView.as_view(), name='listGrupo'),
	path('crearGrupo', GrupoCreateView.as_view(), name='crearGrupo'),
	#Alumno
	path('listAlumno', AlumnosListView.as_view(), name='listAlumno'),
	path('crearAlumno', AlumnoCreateView.as_view(), name='crearAlumno'),
	#Materia
	path('listMateria', MateriasListView.as_view(), name='listMateria'),
	path('crearMateria', MateriaCreateView.as_view(), name='crearMateria'),
	#Problematica
	path('reportes', reportes, name='reportes'),
	path('reportesFechas', reportesFechas, name='reportesFechas'),
	path('fechaRep', fechaRep, name='fechaRep'),
	path('reportesAlumnos', reportesAlumnos, name='reportesAlumnos'),
	path('RepAlum', RepAlum, name='RepAlum'),
	path('reportesGrupos', reportesGrupos, name='reportesGrupos'),
	path('RepGpo', RepGpo, name='RepGpo'),
	path('listProblematica', ProblematicasListView.as_view(), name='listProblematica'),
	path('crearProblematica', ProblematicaCreateView.as_view(), name='crearProblematica'),
	path('updateProblematica/<pk>/', ProblematicaUpdateView.as_view(), name='updateProblematica'),
	path('llenaAl/', llenaAl, name='llenaAl'),
	path('llenaMat/', llenaMat, name='llenaMat'),
]